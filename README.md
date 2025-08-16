# language.py
# 🌍 AI Language Translator

## 🎯 Purpose
- Enables real-time text translation between 7+ languages
- Perfect for travelers, language learners, and multilingual content creators
- Provides offline translation capability (after initial model download)
- Demonstrates practical NLP application using state-of-the-art transformer models

## ✨ Key Features
✅ Simple command-line interface  
✅ Fast inference with MarianMT models  
✅ Supports sentence/phrase translation  
✅ Easily extendable to new language pairs  

*Example translation session (English → French)*

![image alt](https://github.com/rahimanamrina21-hue/language.py/blob/d025d72e72cad0480705b9540d8880a49d7c6c48/3.png)

### Code Overview

The provided code is designed to facilitate language translation. This program prompts the user for source and target languages, then requests text to be translated using a LanguageTranslator instance.

### Code Breakdown

**Functionality**
- **User Inputs**: The program requests:
  - Source language code (e.g., 'en' for English, 'fr' for French)
  - Target language code (e.g., 'fr' for French, 'es' for Spanish)
  - Text that the user wishes to translate

- **Translation Process**:
  - A `LanguageTranslator` instance is created using the provided language codes.
  - The text input by the user is translated using the instance.

- **Output**:
  - The program prints both the original and translated texts.

### Example Outputs

1. **Source Language**:
   - Input: `en` (for English)
   - Target Language: `fr` (for French)

2. **Text to Translate**:
   - Input: "Hi, my name is amrina"

3. **Results**:
   - Original Text: "Hi, my name is amrina"
   - Translated Text: "Bonjour, je m'appelle Amrina."

### Potential Enhancements

- **Error Handling**: Add checks for valid language codes and handle situations where translation might fail.
- **Additional Languages**: Expand support for more language codes and more extensive text inputs.
- **GUI Integration**: Develop a graphical user interface for better user experience.

### User Instructions

To use the code:
1. Copy the script into a Python environment.
2. Run the code and follow the prompts to enter language codes and text for translation.
3. Review the output for both original and translated versions.

### Conclusion

This program serves as a foundational tool for language translation, demonstrating essential input/output processes in programming while facilitating multilingual communication.

![image alt](https://github.com/rahimanamrina21-hue/language.py/blob/aa56d83e71ef99f6c87c138946f245872ed26528/2.png)
