import streamlit as st
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

st.header("Activity 3 - Image Processing")

img_file = st.sidebar.file_uploader('Please input the image path here:', ['png', 'jpg', 'webp', 'jpeg'])

if img_file is not None:
    uploaded_img = Image.open(img_file)
    uploaded_img = np.array(uploaded_img)
    
    rows, cols, dims = uploaded_img.shape
    
    st.sidebar.header('Process Your Image here!')
    user_choice = st.sidebar.slider('Choose an option:', min_value=1, max_value=5, step=1)
    
    # function for translation
    def translation(img_, rows, cols):
        img_translated = np.float32([[1, 0, 50], 
                                     [0, 1, 50],
                                     [0, 0, 1]])
        img_translated = cv2.warpPerspective(img_, img_translated, (cols, rows))
        return img_translated
    
    # function for rotation
    def rotation(img_, rows, cols):
        angle = np.radians(10)
        m_rotated = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
        rotated_img = cv2.warpPerspective(img_, m_rotated, (cols, rows))
        return rotated_img
    
    # function for scaling
    def scaling(img_, rows, cols):
        m_scaling = np.float32([[1.5, 0, 0],
                                [0, 1.8, 0],
                                [0, 0, 1]])
        scaled_img = cv2.warpPerspective(img_, m_scaling, (cols*2, rows*2))
        return scaled_img
    
    # function for reflection
    def reflection(img_, rows, cols):
        m_reflection = np.float32([[1, 0, 0],
                                   [0, -1, rows],
                                   [0, 0, 1]])
        reflected_img = cv2.warpPerspective(img_, m_reflection, (cols, rows))
        return reflected_img
    
    # function for shearing
    def shear(img_, rows, cols):
        m_shearing = np.float32([[1, 0.5, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]])
        sheared_img = cv2.warpPerspective(img_, m_shearing, (int(cols*1.5), int(rows*1.5)))
        return sheared_img
    
    #function that allows the user to choose between the image processing options
    def user_choices(user_choice, img):
        
        if user_choice == 1:
            manipulated_img = translation(img, rows, cols)
    
        elif user_choice == 2:
            manipulated_img  = rotation(img, rows, cols)

        elif user_choice == 3:
            manipulated_img  = scaling(img, rows, cols)

        elif user_choice == 4:
            manipulated_img  = reflection(img, rows, cols)

        elif user_choice == 5:
            manipulated_img  = shear(img, rows, cols)
            
        return manipulated_img 

    img_processed = user_choices(user_choice, uploaded_img)
    st.image(img_processed)

