import streamlit as st
from googletrans import Translator  # Google Translate API

# Streamlit UI
st.title("Language Translation App")

# Input text
text_to_translate = st.text_area("Enter text to translate:", height=150)

# Language selection
source_language = st.selectbox("Choose the source language:",
                               ["English", "Hindi", "Telugu", "Kannada", "Tamil", "Malayalam", "French", "German", "Spanish", "Italian", "Portuguese", "Dutch", "Other"])
target_language = st.selectbox("Choose the target language:",
                               ["English", "Hindi", "Telugu", "Kannada", "Tamil", "Malayalam", "French", "German", "Spanish", "Italian", "Portuguese", "Dutch", "Other"])

# Google Translate API translation function
def translate_with_google(text, source_lang, target_lang):
    translator = Translator()
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    return translated.text

# Translate Button
if st.button("Translate"):
    if text_to_translate:
        # Use Google Translate for all languages
        translated_text = translate_with_google(text_to_translate, source_language, target_language)

        st.subheader("Translated Text:")
        st.write(translated_text)
    else:
        st.warning("Please enter some text to translate.")
