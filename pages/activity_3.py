import cv2
import numpy as np
import streamlit as st

from PIL import Image

def translate(img, x, y):
    M = np.float32([[1, 0, x],
                    [0, 1, y]])
    translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return translated

def rotate(img, theta):
    M = cv2.getRotationMatrix2D((img.shape[1] // 2, img.shape[0] // 2), theta, 1.0)
    rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return rotated

def scale(img, scale):
    M = np.float32([[scale, 0, 0],
                    [0, scale, 0]])
    scaled = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return scaled

def shear(img, x, y):
    M = np.float32([[1, x, 0],
                    [y, 1, 0]])
    sheared = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return sheared

def reflect(img, axis):
    if 'x' in axis.lower():
        reflected = cv2.flip(img, 1)
    if 'y' in axis.lower():
        reflected = cv2.flip(img, 0)
    return reflected

def multiple_image_load():
    images, img_paths = [], []
    c = int(input('Enter number of files: '))
    for i in range(c):
        img_paths.append(input(f'Enter image path {i + 1}/{c} : '))
    for path in img_paths:
        images.append(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB))
    return images

def images_transform(*images):
    transformations = input('Enter transformations to apply to images: ')
    transformed_images = []
    for img in images:
        st.write('Original Image')
        st.image(img)
        if 'translate' in transformations.lower():
            st.write('Translated Image')
            st.image(translate(img, int(input('Enter x translation: ')), int(input('Enter y translation: '))))
        if 'rotate' in transformations.lower():
            st.write('Rotated Image')
            st.image(rotate(img, float(input('Enter rotation angle: '))))
        if 'scale' in transformations.lower():
            st.write('Scaled Image')
            st.image(scale(img, float(input('Enter scale factor: '))))
        if 'shear' in transformations.lower():
            st.write('Sheared Image')
            st.image(shear(img, float(input('Enter x shear factor: ')), float(input('Enter y shear factor: '))))
        if 'reflect' in transformations.lower():
            st.write('Reflected Image')
            st.image(reflect(img, input('Enter axis to reflect image along: ')))
    return transformed_images

def main():
    images = multiple_image_load()
    transformed_images = images_transform(*images)
    st.write('Transformed Images')
    for img in transformed_images:
        st.image(img)

if __name__ == '__
