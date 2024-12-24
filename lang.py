import streamlit as st
from googletrans import Translator
from PIL import Image
import easyocr

# Set up the Streamlit app
def main():
    st.set_page_config(page_title="Indian Language Image Text Translator", layout="wide")
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

    st.markdown("<h1 class='title'>Indian Language Image Text Translator</h1>", unsafe_allow_html=True)
    st.sidebar.header("Upload and Translate")

    uploaded_file = st.sidebar.file_uploader("Upload an image with text", type=["png", "jpg", "jpeg"])
    target_language = st.sidebar.selectbox(
        "Select target language", ["en", "hi", "te", "ta", "kn", "ml", "bn"]
    )  # List of supported Indian languages

    if uploaded_file is not None:
        # Open the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Convert"):
            # Extract text from image
            with st.spinner("Extracting text..."):
                try:
                    # Handle OCR based on the target language
                    if target_language == "ta":
                        reader = easyocr.Reader(["en", "ta"])  # Tamil requires English
                    elif target_language == "ml":
                        reader = easyocr.Reader(["en", "ml"])  # Malayalam requires English
                    else:
                        reader = easyocr.Reader(["en", target_language])  # For other languages

                    extracted_text = "\n".join([text[1] for text in reader.readtext(image)])
                    if not extracted_text.strip():
                        st.warning("No text found in the image.")
                        return
                except Exception as e:
                    st.error(f"Text extraction failed: {str(e)}")
                    return

            st.subheader("Extracted Text:")
            st.text_area("Extracted Text", extracted_text, height=150)

            # Translate text
            translator = Translator()
            with st.spinner("Translating text..."):
                try:
                    translated_text = translator.translate(extracted_text, dest=target_language).text
                except Exception as e:
                    st.error(f"Translation failed: {str(e)}")
                    return

            st.subheader("Translated Text:")
            st.text_area("Translated Text", translated_text, height=150)

if __name__ == "__main__":
    main()
