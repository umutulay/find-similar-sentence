from transformers import pipeline

def french_to_english(input_sentence):
    # Initialize the translation pipeline
    # for more languages, visit this website
    # https://huggingface.co/Helsinki-NLP?sort_models=alphabetical#models
    model_name = "Helsinki-NLP/opus-mt-fr-en"
    translator = pipeline("translation", model=model_name)

    # Perform the translation
    translation = translator(input_sentence, max_length=512)
    # Extract and return the translated text
    translated_text = translation[0]['translation_text']
    return translated_text