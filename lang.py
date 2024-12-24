import streamlit as st
from googletrans import Translator
from PIL import Image
import easyocr
import numpy as np
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

# Test OpenCV Installation
try:
    import cv2
    st.write(f"OpenCV version: {cv2.__version__}")
except ImportError as e:
    st.error(f"Error importing OpenCV: {str(e)}")

# Set up the Streamlit app
def main():
    # Set page config first to avoid errors
    st.set_page_config(page_title="Indian Language Image Text Translator", layout="wide")

    # Add custom styles and header
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

    # Add header with custom style
    st.markdown("<h1 class='title'>Indian Language Image Text Translator</h1>", unsafe_allow_html=True)

    # Option to capture image using webcam (moved above the file uploader)
    st.subheader("Capture Image")
    if st.button("Capture Photo"):
        # Start webcam stream
        webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

    # Option to upload an image file
    uploaded_file = st.file_uploader("Or upload an image with text", type=["png", "jpg", "jpeg"])
    
    # Language selection moved above the file upload
    target_language = st.selectbox(
        "Select target language", ["en", "hi", "te", "ta", "kn", "ml", "bn"]
    )  # List of supported Indian languages

    if uploaded_file is not None:
        # Open the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert PIL image to numpy array
        image_np = np.array(image)

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

                    extracted_text = "\n".join([text[1] for text in reader.readtext(image_np)])
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


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Convert the frame to numpy array
        img = frame.to_ndarray(format="bgr24")
        # Convert to grayscale for easy processing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Save the frame as an image for later processing
        cv2.imwrite("captured_image.jpg", gray)
        st.image(gray, channels="BGR", caption="Captured Image", use_column_width=True)
        return frame


if __name__ == "__main__":
    main()
