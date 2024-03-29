import streamlit as st

st.title("Activity 2")

#activity 2 
#submitted by: group RAM (Reycel Sarmiento, Angelica Nava, Mariane Torreverde) BSCS 1-A


import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[100, 100, 100],  # the numbers inside the array determine the color of the plot area (background), 
                      [100, 100, 100],  # as well as the number of rows & columns)
                      [100, 100, 100]])
    
x = [] #initialization of variables
y = []
replace = []
    
def fill(x, y, replace): # changes the color of one desired position (x,y) you wish to plot in plot area
    
    fig = plt.figure()
    for i in range(len(two_d_arr)):
        for j in range(len(two_d_arr[i])):
            two_d_arr[x][y] = replace
            
    img = plt.imshow(two_d_arr)
    img.set_clim([1,1000])
    plt.colorbar()
    
    return fig
    
    
def main(): #displays & prompt user input, including the instructions or neccesarry informtaion the user has to know. 
    st.sidebar.header("Change Pixel Hue Parameters")
    x = st.sidebar.slider('X coordinate', 0, 2, 0)
    y = st.sidebar.slider('Y coordinate', 0, 2, 0)
    replace = st.sidebar.slider('Hue', 0, 100, 50)
      
    fig_fill = fill(x, y, replace)
    st.subheader("Change pixel hue parameters.")
    st.pyplot(fig_fill)


if __name__ == '__main__':
    main()
