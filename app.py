import streamlit as st
import cv2
import pytesseract as tess
from googletrans import Translator

# --------------------------------------------------
# Tesseract OCR Configuration
# --------------------------------------------------
# If Tesseract is not added to your system PATH,
# uncomment the line below and update it according
# to your installation location.
#
# Example (Windows):
# tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# --------------------------------------------------


def extract_text(image_path, lang="tam"):
    """
    Extract text from an image using Tesseract OCR.
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    extracted_text = tess.image_to_string(image, lang=lang)

    return extracted_text.strip()


def translate_text(text, destination_language="en"):
    """
    Translate extracted text using Google Translator.
    """
    translator = Translator()

    translated = translator.translate(
        text,
        dest=destination_language
    )

    return translated.text


# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------

st.set_page_config(
    page_title="Image Text Extraction & Translation",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Image Text Extraction & Translation")
st.write(
    "Upload an image to extract text using OCR and translate it into another language."
)

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image_path = "temp_image.jpg"

    with open(image_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Extracting text..."):
        extracted_text = extract_text(image_path)

    st.subheader("Extracted Text")

    if extracted_text:
        st.success(extracted_text)
    else:
        st.warning("No text could be extracted from the image.")

    language = st.selectbox(
        "Translate To",
        {
            "English": "en",
            "Hindi": "hi",
            "Tamil": "ta",
            "Telugu": "te",
            "Malayalam": "ml"
        }
    )

    if st.button("Translate"):

        with st.spinner("Translating..."):

            translated_text = translate_text(
                extracted_text,
                language
            )

        st.subheader("Translated Text")
        st.success(translated_text)