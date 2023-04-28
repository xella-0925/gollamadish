The given code is not showing the image in Streamlit. Here is a fixed version of the code that should display the image properly.

```
import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False)

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

# Function to check if file is a valid image
def is_valid_image(file):
    if file is not None and hasattr(file, "type") and file.type.split('/')[1] in ['png', 'jpg', 'webp']:
        return True
    return False

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
if img_file is not None and is_valid_image(img_file):
    uploaded_img = Image.open(img_file)
    uploaded_img = np.array(uploaded_img)
    rows, cols, dims = uploaded_img.shape

    st.write('Original Image:')
    st.image(uploaded_img, use_column_width=True)

    if user_choice == 'Translation':
        st.write('Translated Image:')
        img_processed = translate(uploaded_img, rows, cols)
        st.image(img_processed, use_column_width=True)

    elif user_choice == 'Rotation':
        st.write('Rotated Image:')
        img_processed = rotate(uploaded_img, rows, cols)
        st.image(img_processed, use_column_width=True)

    elif user_choice == 'Scaling':
        st.write('Scaled Image:')
        img_processed = scale(uploaded_img, rows, cols)
        st.image(img_processed, use_column_width=True)

    elif user_choice == 'Reflection':
        st.write('Reflected Image:')
        img_processed = reflect(uploaded_img, rows, cols)
        st.image(img_processed, use_column_width=True)

    elif user_choice == 'Shearing':
        st.write('Sheated Image:')
        img_processed = shear(uploaded_img, rows, cols)
        st.image(img_processed, use_column_width=True)

    if user_choice != 'Select a transformation to apply':
        st.write('Processed Image:')
        st.image(img_processed, use_column_width=True)
    else:
        st.write('No transformation selected')
else:
    st.write('No image selected or invalid file format')

```

Changes Made:

- Added the `use_column_width=True` parameter to the `st.image()` function calls.
- The `use_column_width=True` parameter scales the image to fit the width of the Streamlit column, so that the entire image is visible.
