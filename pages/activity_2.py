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
    
    print("X,Y        X,Y       X,Y")
    print("------------------------")
    print("0,0        0,1       0,2")
    print("1,0        1,1       1,2")
    print("2,0        2,1       2,2")
    
    print()
    
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    replace = int(input("Enter Color (1-1000): "))
    
    fill(x, y, replace) #call function fill to main to plot the matrix. 



if __name__ == '__main__':
    main()
