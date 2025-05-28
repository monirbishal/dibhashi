from transformers import pipeline
def en_to_bn(en_text):
    # Create a translation pipeline for English to Bangla using the provided model.
    translator = pipeline("translation_en_to_bn", model="monirbishal/en-bn-nmt")

    # Example English text to translate.
    # english_text = (
    #     "Artificial intelligence is transforming the way we interact with technology. "
    #     "It is opening new opportunities for innovation and research."
    # )

    # Translate the text.
    translated = translator(en_text, max_length=400)

    # Extract and print the Bangla translation.
    bn_text = translated[0]['translation_text']
    
    return bn_text