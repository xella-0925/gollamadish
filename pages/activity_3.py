import numpy as np
import cv2
import matplotlib.pyplot as plt

# Streamlit app

import streamlit as st
st.title("Activity 3")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Sidebar file uploader widget
st.sidebar.header(" Image Transformations")
uploaded_file = st.sidebar.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Read image
    img_ = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    rows, cols, dims = img_.shape


    # Function to plot transformed image

    def plt_grph(transformed_img_):
        plt.axis('off')
        plt.imshow(transformed_img_)


    # Function to translate image and define its parameters

    def translate(img_, rows, cols, x, y):
        m_translation_ = np.float32([[1, 0, x],
                                    [0, 1, y],
                                    [0, 0, 1]])
        translated_img_ = cv2.warpPerspective(img_, m_translation_, (cols, rows))
        return translated_img_


    # Function to scale image and define its parameters

    def scaling(img_, rows, cols, x, y):
        m_scaling_ = np.float32([[x, 0, 0],
                                 [0, y, 0],
                                 [0, 0, 1]])
        scaled_img_ = cv2.warpPerspective(img_, m_scaling_, (int(cols*x), int(rows*y)))
        return scaled_img_


    # Function to rotate image and define its parameters

    def rotate(img_, rows, cols, angle):
        m_rotation_ = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
        rotated_img_ = cv2.warpAffine(img_, m_rotation_, (cols, rows))
        return rotated_img_


    # Function to flip image and define its parameters

    def flip(img_, axis):
        img_flipped_ = cv2.flip(img_, axis)
        return img_flipped_


    # Function to shear image (x) and define its parameters

    def shear_x(img_, rows, cols, factor):
        m_shearing_x = np.float32([[1, factor, 0],
                                   [0, 1, 0],
                                   [0, 0, 1]])
        sheared_img_x = cv2.warpPerspective(img_, m_shearing_x, (int(cols*1.5), int(rows*1.5)))
        return sheared_img_x


    # Function to shear image (y) and define its parameters

    def shear_y(img_, rows, cols, factor):
        m_shearing_y = np.float32([[1, 0, 0],
                                   [factor, 1, 0],
                                   [0, 0, 1]])
        sheared_img_y = cv2.warpPerspective(img_, m_shearing_y, (int(cols*1.5), int(rows*1.5)))
        return sheared_img_y


    # Sidebar slider widget
    option = st.sidebar.selectbox("Select Transformation", ["Original Image",
                                                            "Translation",
                                                            "Scaling",
                                                            "Rotation",
                                                            "Flip",
                                                            "Shear (X)",
                                                            "Shear (Y)"])

    if option == "Original Image":
        # Displays the original image
        st.subheader("Original Image")
        st.image(img_, use_column_width=True)

    elif option == "Translation":
        # Translation Parameters
        x = st.sidebar.slider("Horizontal Shift", -200, 200, 100)
        y = st.sidebar.slider("Vertical Shift", -200, 200, 50)
        result = translate(img_, rows, cols, x, y)
        plt_grph(result)
        st.subheader("Translated Image")
        st.pyplot()

    elif option == "Scaling":
        # Scaling Parameters
        x = st.sidebar.slider("Horizontal Scaling Factor", 0.1, 5.0, 1.5, 0.1)
        y = st.sidebar.slider("Vertical Scaling Factor", 0.1, 5.0, 1.8, 0.1)
        result = scaling(img_, rows, cols, x, y)
        plt_grph(result)
        st.subheader("Scaled Image")
        st.pyplot()

    elif option == "Rotation":
        # Rotation Parameters
        angle = st.sidebar.slider("Angle of Rotation", -180, 180, 10)
        result = rotate(img_, rows, cols, angle)
        plt_grph(result)
        st.subheader("Rotated Image")
        st.pyplot()

    elif option == "Flip":
        # Flipping Parameters
        axis = st.sidebar.slider("Flip Axis", 0, 1, 1)
        result = flip(img_, axis)
        plt_grph(result)
        st.subheader("Flipped Image")
        st.pyplot()

    elif option == "Shear (X)":
        # Shearing (X) Parameters
        factor = st.sidebar.slider("Shear Factor", -1.0, 1.0, 0.2, 0.01)
        result = shear_x(img_, rows, cols, factor)
        plt_grph(result)
        st.subheader("Sheared(X) Image")
        st.pyplot()

    elif option == "Shear (Y)":
        # Shearing (Y) Parameters
        factor = st.sidebar.slider("Shear Factor", -1.0, 1.0, 0.2, 0.01)
        result = shear_y(img_, rows, cols, factor)
        plt_grph(result)
        st.subheader("Sheared(Y) Image")
        st.pyplot()
