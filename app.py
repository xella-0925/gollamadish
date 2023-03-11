import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pages.activity_1 as act1

def main():
    st.title("Midterm Exam in CCS221")
    
    st.sidebar.header("Line Algorithm Parameters")
    _act1_x0, _act1_y0, _act1_x1, _act1_y1 = st.sidebar.slider('Starting X', 1, 1000), \
                     st.sidebar.slider('Starting Y', 1, 1000), \
                     st.sidebar.slider('Ending X', 1, 1000, 100), \
                     st.sidebar.slider('Ending Y', 1, 1000, 100)
    
    st.header("Task 1")
    st.subheader("DDA Line Algorithm")
    st.pyplot(act1.DDALine(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Bresenham's Line Algorithm")
    st.pyplot(act1.bresenham(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Midpoint Line Algorithm")
    st.pyplot(act1.midpoint(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))

        if st.button("Exit"):
        st.stop()

if  __name__ == "__main__":
    main()
    

