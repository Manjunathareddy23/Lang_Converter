import streamlit as st
from googletrans import Translator, LANGUAGES  

# Apply custom CSS using st.markdown
st.markdown("""
    <style>
    /* Set full-page background color to navy blue */
    [data-testid="stAppViewContainer"] {
        background-color: #000080 !important; /* Navy Blue */
    }

    /* Title Styling - Highlighting the main heading */
    h1 {
        background-color: #FFD700; /* Gold background */
        color: #FFFFFF; /* White text */
        text-align: center;
        font-size: 2.5rem;
        padding: 20px;
        border-radius: 10px;
    }

    /* Style the text area with white background */
    textarea {
        background-color: #FFFFFF !important; /* White */
        color: black;
        font-size: 16px;
        font-weight: bold;
        border: 2px solid #32CD32; /* Lime Green Border */
        border-radius: 10px;
        padding: 10px;
    }

    /* Style select dropdowns with light green */
    [data-testid="stSelectbox"] {
        background-color: #90EE90 !important; /* Light Green */
        border-radius: 10px;
        border: 2px solid #32CD32; /* Lime Green */
        padding: 5px;
    }

    /* Style translate button */
    [data-testid="stButton"] button {
        background-color: #FF1493 !important; /* Dark Pink */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        transition: 0.3s;
    }

    /* Hover effect for button */
    [data-testid="stButton"] button:hover {
        background-color: #D6006E !important;
    }

    /* Style translated text with white background */
    .translated-text {
        background-color: #FFFFFF !important; /* White */
        color: black;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }

    /* Style success message with pink background */
    .success-message {
        background-color: #FFC0CB !important; /* Pink */
        color: black;
        padding: 10px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: bold;
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
        st.markdown(f'<div class="translated-text">Translated Text: {translated_text}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text to translate.")

# Success message with pink background
st.markdown('<div class="success-message">Developed by K.Manjunathareddy-6300138360</div>', unsafe_allow_html=True)
