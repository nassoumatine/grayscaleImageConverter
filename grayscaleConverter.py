"""
This file converts a photo from the user to greyscale
"""
import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to  grayscale
    gray_img = img.convert("L")

    # Display the grayscale image on the webpage
    st.image(gray_img)

if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)

    # Convert the pillow image to  grayscale
    gray_img = img.convert("L")

    # Display the grayscale image on the webpage
    st.image(gray_img)
