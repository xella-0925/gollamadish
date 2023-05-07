import numpy as np
import cv2
import matplotlib.pyplot as plt

import streamlit as st
st.title("Quiz 1 - Translation")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Sidebar file uploader widget
st.sidebar.header("Image Transformations")
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

    no_of_imgs = st.sidebar.slider("Number of Images:", 0, 100, step=1)

    for no_of_tests in range(no_of_imgs):
        Bx_old = st.sidebar.slider(f"Bx_old_{no_of_tests}", 0, cols, step=1)
        By_old = st.sidebar.slider(f"By_old_{no_of_tests}", 0, rows, step=1)

        Tx = st.sidebar.slider(f"Tx_{no_of_tests}", -cols, cols, step=1)
        Ty = st.sidebar.slider(f"Ty_{no_of_tests}", -rows, rows, step=1)

        Bx_new = Bx_old + Tx
        By_new = By_old + Ty

        old_img = translate(img_, rows, cols, Bx_old, By_old)
        plt.figure()
        plt_grph(old_img)

        new_img = translate(img_, rows, cols, Bx_new, By_new)
        plt.figure()
        plt_grph(new_img)
