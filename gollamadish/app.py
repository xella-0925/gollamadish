import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pages.activity_1 as act1
import pages.activity_2 as act2
import pages.activity_3 as act3

st.set_option('deprecation.showPyplotGlobalUse', False)
#st.set_option ('browser.gatherUsageStats' , False)

def main():
    st.title("Midterm Exam in CCS221")

    st.sidebar.header("Line Algorithm Parameters")
    _act1_x0, _act1_y0, _act1_x1, _act1_y1 = st.sidebar.slider('Starting X', 1, 100), \
                     st.sidebar.slider('Starting Y', 1, 100), \
                     st.sidebar.slider('Ending X', 1, 100, 10), \
                     st.sidebar.slider('Ending Y', 1, 100, 10)

    st.sidebar.header("Change Pixel Hue Parameters")
    _act2_x, _act2_y, _act2_hue = st.sidebar.slider('X coordinate', 0, 2, 0, 1), \
                                     st.sidebar.slider('Y coordinate', 0, 2, 0, 1), \
                                     st.sidebar.slider('Hue', 0, 100, 50)

    st.sidebar.header("Image transformations")
    _act3_filepath = st.sidebar.text_input('Enter file path: ', 'pages/biniarms.webp')

    _act3_transformations = st.sidebar.multiselect('Select tranformations to apply: ', \
                            ['translate', 'rotate', 'reflect', 'scale', 'shear'])

    if 'translate' in _act3_transformations:
        _act3_translated_imgx = st.sidebar.slider('X Translation', 0, 1000)
        _act3_translated_imgy = st.sidebar.slider('Y Translation', 0, 1000)

    if 'reflect' in _act3_transformations:
        _act3_reflected_imgx = st.sidebar.checkbox('Reflect along x axis')
        _act3_reflected_imgy = st.sidebar.checkbox('Reflect along y axis')

    if 'rotate' in _act3_transformations:
        _act3_rotated_img = st.sidebar.slider('Rotation', -360, 360, 0)

    if 'scale' in _act3_transformations:
        _act3_scaled_img = st.sidebar.slider('Scale', 0, 5, 1)

    if 'shear' in _act3_transformations:
        _act3_sheared_imgx = st.sidebar.slider('X Shear', 0, 5, 1)
        _act3_sheared_imgy = st.sidebar.slider('Y Shear', 0, 5, 1)


    st.header("Activity 1")
    st.subheader("DDA Line Algorithm")
    st.pyplot(act1.DDALine(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Bresenham's Line Algorithm")
    st.pyplot(act1.bresenham(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Midpoint Line Algorithm")
    st.pyplot(act1.midpoint(_act1_x0, _act1_y0, _act1_x1, _act1_y1))

    st.header("Activity 2")
    st.subheader("Change a pixel's color")
    st.pyplot(act2.fill(_act2_x, _act2_y, _act2_hue))

    st.header("Activity 3")
    st.subheader("Image Transformations")
    st.write('File Path: ', _act3_filepath)
    act3_image = cv2.cvtColor(cv2.imread(_act3_filepath), cv2.COLOR_BGR2RGB)
    st.write('Original Image:')
    st.pyplot(act3.visualize(act3_image))
    st.write('Image Transformations: ', *_act3_transformations)
    
    if st.button("Exit"):
        st.stop()

if  __name__ == "__main__":
    main()
