import os
import numpy as np
import evaluate
from datasets import load_dataset, Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer
)

def traning_model():
    # === Load existing model/tokenizer
    model_name = "monirbishal/en-bn-nmt"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # === Load new data JSON: [{"en": "...", "bn": "..."}]
    new_ds = load_dataset("json", data_files="src/dibhashi/static/traning/data.json", field=None)["train"]

    # === Tokenize new examples
    def preprocess(ex):
        enc = tokenizer(ex["en"], truncation=True, padding="max_length", max_length=128)
        dec = tokenizer(text_target=ex["bn"], truncation=True, padding="max_length", max_length=128)
        enc["labels"] = dec["input_ids"]
        return enc

    tokenized_new = new_ds.map(preprocess, batched=True, remove_columns=["en", "bn"])

    # === Optionally load previous combined dataset and concatenate
    # combined = load_dataset("path/to/combined_ds")  # if you saved before
    # full_ds = concatenate_datasets([combined["train"], tokenized_new])
    # For now, just train on new data only:
    full_ds = tokenized_new.train_test_split(test_size=0.1)

    # === Data collator
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    # === Metric for evaluation
    sacrebleu = evaluate.load("sacrebleu")
    def compute_metrics(eval_pred):
        preds, labels = eval_pred
        if isinstance(preds, tuple): preds = preds[0]
        decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
        labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
        decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
        decoded_labels = [[lbl] for lbl in decoded_labels]
        return {"bleu": sacrebleu.compute(predictions=decoded_preds, references=decoded_labels)["score"]}

    # === Training setup
    args = Seq2SeqTrainingArguments(
        output_dir="updated-model",
        overwrite_output_dir=True,
        evaluation_strategy="epoch",
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        num_train_epochs=3,
        save_total_limit=2,
        predict_with_generate=True,
        fp16=True,
        logging_steps=50,
    )

    # === Trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=args,
        train_dataset=full_ds["train"],
        eval_dataset=full_ds["test"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics
    )

    # === Fine-tune
    trainer.train()
    trainer.save_model("fine-tuned-en-bn-updated")
    tokenizer.save_pretrained("fine-tuned-en-bn-updated")