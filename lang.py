import streamlit as st
from deep_translator import GoogleTranslator

# Apply custom CSS using st.markdown
st.markdown("""
    <style>
    /* Set full-page background color to navy blue */
    [data-testid="stAppViewContainer"] {
        background-color: #000080 !important;
    }

    /* Title Styling */
    h1 {
        background-color: #FFD700;
        color: #FFFFFF;
        text-align: center;
        font-size: 2.5rem;
        padding: 20px;
        border-radius: 10px;
    }

    /* Text Area */
    textarea {
        background-color: #FFFFFF !important;
        color: black !important;
        font-size: 16px;
        font-weight: bold;
        border: 2px solid #32CD32;
        border-radius: 10px;
        padding: 10px;
    }

    /* Dropdowns */
    [data-testid="stSelectbox"] {
        background-color: #90EE90 !important;
        border-radius: 10px;
        border: 2px solid #32CD32;
        padding: 5px;
    }

    /* Button */
    [data-testid="stButton"] button {
        background-color: #FF1493 !important;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        transition: 0.3s;
    }

    [data-testid="stButton"] button:hover {
        background-color: #D6006E !important;
    }

    /* Output Box */
    .translated-text {
        background-color: #FFFFFF !important;
        color: black;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        margin-top: 15px;
    }

    /* Footer */
    .success-message {
        background-color: #FFC0CB !important;
        color: black;
        padding: 10px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: bold;
        margin-top: 20px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌍 Language Translation App 🇮🇳")

# Text Input
text_to_translate = st.text_area(
    "Enter text to translate:",
    height=150
)

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Tamil": "ta",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl"
}

# Dropdowns
source_language = st.selectbox(
    "Choose the source language:",
    list(languages.keys())
)

target_language = st.selectbox(
    "Choose the target language:",
    list(languages.keys())
)

# Translation Function
def translate_with_google(text, source_lang, target_lang):
    translated = GoogleTranslator(
        source=languages[source_lang],
        target=languages[target_lang]
    ).translate(text)

    return translated

# Translate Button
if st.button("Translate 🔄"):

    if text_to_translate.strip() == "":
        st.warning("⚠️ Please enter some text to translate.")

    elif source_language == target_language:
        st.warning("⚠️ Source and target languages cannot be the same.")

    else:
        try:
            translated_text = translate_with_google(
                text_to_translate,
                source_language,
                target_language
            )

            st.markdown(
                f'''
                <div class="translated-text">
                    <b>Translated Text:</b><br><br>
                    {translated_text}
                </div>
                ''',
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Translation Error: {e}")

# Footer
st.markdown(
    '<div class="success-message">Developed by K.Manjunathareddy - 6300138360</div>',
    unsafe_allow_html=True
)
