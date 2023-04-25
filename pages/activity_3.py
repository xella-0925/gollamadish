import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title='Image Processing', page_icon=':camera:')
st.title('Image Processing')

# Sidebar for uploading image and selecting transformations
st.sidebar.title('Image transformations')
img_file = st.sidebar.file_uploader('Upload your files here', ['png', 'jpg', 'webp'], True)
user_choice = st.sidebar.selectbox('Select a transformation to apply', ['Translation', 'Rotation', 'Scaling', 'Reflection', 'Shearing'])

# Function for displaying image with matplotlib
def visualize(img):
    st.image(img, use_column_width=True)

# Function for applying image transformation
def apply_transformation(img_, transformation_matrix):
    transformed_img = cv2.warpPerspective(img_, transformation_matrix, (img_.shape[1], img_.shape[0]))
    return transformed_img

# Transformation matrices
translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]])
rotation_matrix = cv2.getRotationMatrix2D((0, 0), 10, 1)
scale_matrix = np.float32([[1.5, 0, 0], [0, 1.8, 0], [0, 0, 1]])
reflection_matrix = np.float32([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
shearing_matrix = np.float32([[1, 0.2, 0], [0.3, 1, 0], [0, 0, 1]])

# Main code for processing image and displaying transformed images
if img_file is not None:
    uploaded_img = Image.open(img_file)
    uploaded_img = np.array(uploaded_img)

    st.write('Original Image:')
    visualize(uploaded_img)

    if user_choice == 'Translation':
        st.write('Translated Image:')
        visualize(apply_transformation(uploaded_img, translation_matrix))

    elif user_choice == 'Rotation':
        st.write('Rotated Image:')
        visualize(apply_transformation(uploaded_img, rotation_matrix))

    elif user_choice == 'Scaling':
        st.write('Scaled Image:')
        visualize(apply_transformation(uploaded_img, scale_matrix))

    elif user_choice == 'Reflection':
        st.write('Reflected Image:')
        visualize(apply_transformation(uploaded_img, reflection_matrix))

    elif user_choice == 'Shearing':
        st.write('Sheared Image:')
        visualize(apply_transformation(uploaded_img, shearing_matrix))
