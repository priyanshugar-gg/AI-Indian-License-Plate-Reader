import streamlit as st
import tempfile
import cv2
import numpy as np
from paddleocr import PaddleOCR
from PIL import Image

#Setting page configuration
st.set_page_config(page_title="Indian License Plate Reader", layout="centered")

st.title("AI Indian License Plate Reader")
st.write("Upload an image of an Indian License Plate to extract the registration number.")

#Streamlit file uploader widget
uploaded_files = st.file_uploader("Choose an images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

def load_and_preprocess_image_pil(pil_img):
    #Converting to grayscale and then to numpy array for better processing.
    img_gray = pil_img.convert('L')
    np_img = np.array(img_gray)
    _, binary = cv2.threshold(np_img, 127, 255, cv2.THRESH_BINARY)
    return binary

def find_image_contours_pil(pil_img):
    binary = load_and_preprocess_image_pil(pil_img)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours_pil(pil_img, contours):
    np_img = np.array(pil_img.convert('RGB'))
    contoured_img = cv2.drawContours(np_img.copy(), contours, -1, (0, 255, 0), 2)
    return contoured_img

if uploaded_files:
    # Initialize OCR engine once for all images
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_container_width=True)

        # Draw contours
        contours = find_image_contours_pil(image)
        contoured = draw_contours_pil(image, contours)
        st.image(contoured, caption=f"Contours: {uploaded_file.name}", use_container_width=True)

        # OCR processing
        with st.spinner(f'Running OCR on {uploaded_file.name}...'):
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp:
                temp_img_path = temp.name
                image.save(temp_img_path)
                result = ocr.ocr(temp_img_path)

            if not result or len(result) == 0:
                st.error(f"No text found in {uploaded_file.name}.")
            else:
                rec_texts = result[0].get("rec_texts", [])
                rec_scores = result[0].get("rec_scores", [])
                if rec_texts:
                    st.subheader(f"All Detected Text Boxes for {uploaded_file.name}")
                    for text, conf in zip(rec_texts, rec_scores):
                        st.write(f"Detected: '{text}' (Confidence: {conf:.2f})")
                    best_idx = int(np.argmax(rec_scores))
                    st.success(f"Possible License Plate Text for {uploaded_file.name}:")
                    st.code(rec_texts[best_idx])
                else:
                    st.error(f"No text found in {uploaded_file.name}.")
else:
    st.info("Please upload one or more images to continue.")


