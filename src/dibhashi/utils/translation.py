from transformers import pipeline
def en_to_bn(en_text):
    translator = pipeline("translation_en_to_bn", model="monirbishal/en-bn-nmt")
    translated = translator(en_text, max_length=400)
    bn_text = translated[0]['translation_text']
    
    return bn_text