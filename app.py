import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pages.activity_1 as act1
import pages.activity_2 as act2

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("Midterm Exam in CCS221")
    
    st.sidebar.header("Line Algorithm Parameters")
    _act1_x0, _act1_y0, _act1_x1, _act1_y1 = st.sidebar.slider('Starting X', 1, 500), \
                     st.sidebar.slider('Starting Y', 1, 500), \
                     st.sidebar.slider('Ending X', 1, 500, 100), \
                     st.sidebar.slider('Ending Y', 1, 500, 100)
    
    st.header("Activity 2")
    st.sidebar.header("Change Pixel Hue Parameters")
    _act2_x, _act2_y, _act2_hue = st.sidebar.slider('X coordinate', 0, 2, 0, 1), \
                                     st.sidebar.slider('Y coordinate', 0, 2, 0, 1), \
                                     st.sidebar.slider('Hue', 0, 100, 50)
    
    st.header("Activity 1")
    st.subheader("DDA Line Algorithm")
    st.pyplot(act1.DDALine(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Bresenham's Line Algorithm")
    st.pyplot(act1.bresenham(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Midpoint Line Algorithm")
    st.pyplot(act1.midpoint(_act1_x0, _act1_y0, _act1_x1, _act1_y1))
    
    st.header("Task 2")
    st.subheader("Change a pixel's color")
    st.pyplot(task2.fill(_task2_x, _task2_y, _task2_hue))
       
    if st.button("Exit"):
        st.stop()

if  __name__ == "__main__":
    main()
    

