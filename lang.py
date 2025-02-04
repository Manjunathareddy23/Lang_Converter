import streamlit as st
from googletrans import Translator, LANGUAGES  

# Apply custom CSS directly in the app
st.markdown("""
    <style>
    /* Set full-page background color to cyan */
    body {
        background-color: cyan !important; /* Cyan */
    }

    /* Title Styling */
    h1 {
        color: #003366; /* Dark Blue */
        text-align: center;
        font-size: 2.5rem;
    }

    /* Style the text area with pink */
    .stTextArea textarea {
        background-color: #FFC0CB !important; /* Pink */
        color: black;
        font-size: 16px;
        font-weight: bold;
        border: 2px solid #FF1493; /* Dark Pink Border */
        border-radius: 10px;
        padding: 10px;
    }

    /* Style select dropdowns */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFC0CB !important; /* Pink */
        border-radius: 10px;
        border: 2px solid #FF1493; /* Dark Pink */
        padding: 5px;
    }

    /* Style translate button */
    .stButton button {
        background-color: #FF1493 !important; /* Dark Pink */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        transition: 0.3s;
    }

    /* Hover effect for button */
    .stButton button:hover {
        background-color: #D6006E !important;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("🌍 Language Translation App 🇮🇳")

# Input text
text_to_translate = st.text_area("Enter text to translate:", height=150)

# Language selection
languages = {
    "English": "en", "Hindi": "hi", "Telugu": "te", "Kannada": "kn", "Tamil": "ta",
    "Malayalam": "ml", "French": "fr", "German": "de", "Spanish": "es", "Italian": "it",
    "Portuguese": "pt", "Dutch": "nl"
}

source_language = st.selectbox("Choose the source language:", list(languages.keys()))
target_language = st.selectbox("Choose the target language:", list(languages.keys()))

# Google Translate API translation function
def translate_with_google(text, source_lang, target_lang):
    translator = Translator()
    translated = translator.translate(text, src=languages[source_lang], dest=languages[target_lang])
    return translated.text

# Translate Button
if st.button("Translate 🔄"):
    if text_to_translate:
        translated_text = translate_with_google(text_to_translate, source_language, target_language)
        st.subheader("Translated Text:")
        st.write(translated_text)
    else:
        st.warning("⚠️ Please enter some text to translate.")
st.success("Developed by K.Manjunathareddy-6300138360")
