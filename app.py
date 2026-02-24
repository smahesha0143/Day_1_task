from googletrans import Translator

translator = Translator()

print("=== Text to English Translator ===")

# User input
text = input("Enter text: ")
source_lang = input("Enter source language code (like ta, hi, kn, te, ml, fr, etc): ")

# Translate to English
translated = translator.translate(text, src=source_lang, dest='en')

print("Translated to English:", translated.text)