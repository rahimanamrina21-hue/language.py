from transformers import MarianMTModel, MarianTokenizer

class LanguageTranslator:
    def __init__(self, src_lang, tgt_lang):
        # Define the model name based on source and target languages
        self.model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
        self.model = MarianMTModel.from_pretrained(self.model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)

    def translate(self, text):
        # Tokenize the input text
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        # Perform the translation
        translated = self.model.generate(**inputs)
        # Decode the translated text
        translated_text = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return translated_text

if __name__ == "__main__":
    # Get user input for source and target languages, clarifying that codes are needed
    src_lang = input("Enter source language code (e.g., 'en' for English, 'fr' for French): ")
    tgt_lang = input("Enter target language code (e.g., 'fr' for French, 'es' for Spanish): ")

    # Create a translator instance
    translator = LanguageTranslator(src_lang, tgt_lang)

    # Get the text to translate from the user
    text_to_translate = input("Enter the text to translate: ")

    # Perform the translation
    translated_text = translator.translate(text_to_translate)

    # Print the results
    print(f"Original Text: {text_to_translate}")
    print(f"Translated Text: {translated_text}")
