import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

st.header("Activity 3 - Image Processing")

# Sidebar for uploading image and selecting transformations
st.sidebar.header("Image transformations")
img_file = st.sidebar.file_uploader('Upload your files here', ['png', 'jpg', 'webp'], True)
user_choice = st.sidebar.selectbox('Select a transformation to apply', ['Translation', 'Rotation', 'Scaling', 'Reflection', 'Shearing'])

# Function for displaying image with matplotlib
def visualize(img):
    plt.imshow(img)
    plt.axis('off')
    plt.tight_layout()
    # return the plotted image as a numpy array
    return np.array(plt.gcf().canvas.buffer_rgba())


# Function for translation
def translate(img_, rows, cols):
    img_translated = np.float32([[1, 0, cols//4], 
                                 [0, 1, rows//4],
                                 [0, 0, 1]])
    img_translated = cv2.warpPerspective(img_, img_translated, (cols, rows))
    return img_translated

# Function for rotation
def rotate(img_, rows, cols):
    angle = np.radians(10)
    m_rotated = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                            [np.sin(angle), np.cos(angle), 0],
                            [0, 0, 1]])

    rotated_img = cv2.warpPerspective(img_, m_rotated, (int(cols), int(rows)))
    return rotated_img

# Function for scaling
def scale(img_, rows, cols):
    m_scaling = np.float32([[1.5, 0, 0],
                            [0, 1.8, 0],
                            [0, 0, 1]])
    scaled_img = cv2.warpPerspective(img_, m_scaling, (cols*2, rows*2))
    return scaled_img

# Function for reflection
def reflect(img_, rows, cols):
    m_reflection = np.float32([[1, 0, 0],
                               [0, -1, rows],
                               [0, 0, 1]])
    reflected_img = cv2.warpPerspective(img_, m_reflection, (cols, rows))
    return reflected_img

# Function for shearing
def shear(img_, rows, cols):
    m_sheared = np.float32([[1, 0.2, 0],
                            [0.3, 1, 0],
                            [0, 0, 1]])
    sheared_img = cv2.warpPerspective(img_, m_sheared, (cols, rows))
    return sheared_img

# Main code for processing image and displaying transformed images
# Main code for processing image and displaying transformed images
if img_file is not None:
    uploaded_img = Image.open(img_file)
    uploaded_img = np.array(uploaded_img)
    rows, cols, dims = uploaded_img.shape

    st.write('Original Image:')
    st.image(uploaded_img)

    if user_choice == 'Translation':
        st.write('Translated Image:')
        st.image(translate(uploaded_img, rows, cols))

    elif user_choice == 'Rotation':
        st.write('Rotated Image:')
        st.image(rotate(uploaded_img, rows, cols))

    elif user_choice == 'Scaling':
        st.write('Scaled Image:')
        st.image(scale(uploaded_img, rows, cols))

    elif user_choice == 'Reflection':
        st.write('Reflected Image:')
        st.image(reflect(uploaded_img, rows, cols))

    elif user_choice == 'Shearing':
        st.write('Sheated Image:')
        st.image(shear(uploaded_img, rows, cols))

    if user_choice != 'Select a transformation to apply':
        st.write('Processed Image:')
        st.image(visualize(img_processed))

else:
    default_img = np.zeros((256, 256, 3), dtype=np.uint8)
    st.image(default_img, caption='Upload an image to apply transformations')


    st.write('Processed Image:')
    st.image(img_processed)
