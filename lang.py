import streamlit as st
from googletrans import Translator
from PIL import Image
import pytesseract
import io
import base64

# Set up the Streamlit app
def main():
    st.set_page_config(page_title="Image Text Translator", layout="wide")
    st.markdown(
        """
        <style>
        body {
            background-color: #f7f7f7;
        }
        .title {
            text-align: center;
            color: #4CAF50;
            font-family: Arial, sans-serif;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 class='title'>Image Text Translator</h1>", unsafe_allow_html=True)

    st.sidebar.header("Upload and Translate")

    uploaded_file = st.sidebar.file_uploader("Upload an image with text", type=["png", "jpg", "jpeg"])
    target_language = st.sidebar.selectbox("Select target language", ["en","te", "ta", "kn", "ml", "ka"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert the image to text using pytesseract
        with st.spinner("Extracting text..."):
            extracted_text = pytesseract.image_to_string(image)

        st.subheader("Extracted Text:")
        st.text_area("", extracted_text, height=150)

        if st.button("Translate Text"):
            if extracted_text.strip():
                translator = Translator()
                with st.spinner("Translating..."):
                    translated_text = translator.translate(extracted_text, dest=target_language).text

                st.subheader("Translated Text:")
                st.text_area("", translated_text, height=150)
            else:
                st.warning("No text found to translate.")

if __name__ == "__main__":
    main()
