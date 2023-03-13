import streamlit as st

st.title("Activity 2")

import numpy as np #Import libraries needed
import cv2
import matplotlib.pyplot as plt

img_ = cv2.imread("bini.jpg") #use imread to load an image from the specified file and return it
img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB) #use cvtColor to convert image from one color space to another.
                                             # cv2. COLOR_BGR2RGB returns image in RGB format.
  
  rows, cols, dims = img_.shape #define img.shape 
                              #img.shape returns a tuple of the number of rows, columns
def plt_grph(transformed_img_): #create a function to plot transformed image image
    plt.axis('off') #hide axes and borders
    plt.imshow(transformed_img_) #display data as an image
    
 def translate (img_, rows, cols): #create def function to translate image and define its parameters.
    m_translation_ = np.float32 ([[1, 0, 100], #create an array to determine the number of rows and columns of an image.
                                  [0, 1, 50],
                                  [0, 0, 1]])
                                  
    translated_img_ = cv2.warpPerspective(img_, m_translation_, (cols, rows)) #return an image whose size is 
                                                                              #the same as the size of the original image. 

    return translated_img_ 
  
  result = translate (img_, rows, cols) # create a new variable called "result" and assign the function "translate" to it
                                      #so that the function can easily be called, which inreases code reusability. 
plt_grph(result) #call graph function and add "result" as its parameter to dispaly image.
