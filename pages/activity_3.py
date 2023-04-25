import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st

def translate(img, x, y):
    '''
    Translates an image (img) along the x and y axes by (x, y) pixels.
    Returns the translated image.
    
    Parameters:
    img: image to be translated
    x: number of pixels to translate the image along the x axis
    y: number of pixels to translate the image along the y axis
    '''
    M = np.float32([[1, 0, x],
                     [0, 1, y]])
    translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return translated

def rotate(img, theta):
    '''
    Rotates an image (img) by an angle (theta) in degrees.
    Returns the rotated image.
    
    Parameters:
    img: image to be rotated
    theta: angle in degrees to rotate the image
    '''
    M = cv2.getRotationMatrix2D((img.shape[1] // 2, img.shape[0] // 2), theta, 1.0)
    rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return rotated

def scale(img, scale):
    '''
    Scales an image (img) by a factor of (scale).
    Returns the scaled image.
    
    Parameters:
    img: image to be scaled
    scale: factor to scale the image by
    '''
    M = np.float32([[scale, 0, 0],
                    [0, scale, 0]])
    scaled = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return scaled

def shear(img, x, y):
    '''
    Shears an image (img) by a factor to its length (y) and width (w).
    Returns the sheared image.
    
    Parameters:
    img: image to be sheared
    x: factor to shear the image along the x axis
    y: factor to shear the image along the y axis
    '''
    M = np.float32([[1, x, 0],
                    [y, 1, 0]])
    sheared = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return sheared

def reflect(img, axis):
    '''
    Reflects an image (img) along an axis (axis).
    Returns the reflected image.
    
    Parameters:
    img: image to be reflected
    axis: axis to reflect the image along
    '''
    if 'x' in axis.lower():
        reflected = cv2.flip(img, 1)
    if 'y' in axis.lower():
        reflected = cv2.flip(img, 0)
    return reflected

def visualize(img):
    fig = plt.figure()
    plt.imshow(img)
    plt.axis('off')
    return fig
def upload_images():
    '''
    Uploads multiple images from the user and returns a list of images.
    '''

    images = []
    uploaded_files = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)

    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            image = np.array(image)
            images.append(image)
    return images

def images_transform():
    '''
    Transforms multiple images (images) using the functions defined above.
    Prompts the user to enter the parameters for each transformation.
    '''

    images = upload_images()

    transformations = st.sidebar.multiselect('Select transformations to apply to images:', 
                                             ['translate', 'rotate', 'scale', 'shear', 'reflect'],
                                             format_func=str)

    for img in images:
        st.subheader('Original Image')
        st.image(img, use_column_width=True)

        if 'translate' in transformations:
            x_translation = st.slider('X Translation', -img.shape[1], img.shape[1], 0)
            y_translation = st.slider('Y Translation', -img.shape[0], img.shape[0], 0)
            transformed_img = translate(img, x_translation, y_translation)
            st.subheader('Translated Image')
            st.image(transformed_img, use_column_width=True)
            img = transformed_img

        if 'rotate' in transformations:
            rotation_angle = st.slider('Rotation Angle', -180.0, 180.0, 0.0)
            transformed_img = rotate(img, rotation_angle)
            st.subheader('Rotated Image')
            st.image(transformed_img, use_column_width=True)
            img = transformed_img

        if 'scale' in transformations:
            scale_factor = st.slider('Scale Factor', 0.1, 10.0, 1.0, 0.1)
            transformed_img = scale(img, scale_factor)
            st.subheader('Scaled Image')
            st.image(transformed_img, use_column_width=True)
            img = transformed_img

        if 'shear' in transformations:
            x_shear_factor = st.slider('X Shear Factor', -1.0, 1.0, 0.0, 0.1)
            y_shear_factor = st.slider('Y Shear Factor', -1.0, 1.0, 0.0, 0.1)
            transformed_img = shear(img, x_shear_factor, y_shear_factor)
            st.subheader('Sheared Image')
            st.image(transformed_img, use_column_width=True)
            img = transformed_img

        if 'reflect' in transformations:
            reflection_axis = st.radio('Select axis to reflect the image along:', ['X axis', 'Y axis'])
            transformed_img = reflect(img, reflection_axis)
            st.subheader('Reflected Image')
            st.image(transformed_img, use_column_width=True)
            img = transformed_img


            
def main():

    imgs = multiple_image_load()
    images_transform(*imgs)
    
    st.sidebar.header("Image transformations")
    _act3_images = st.sidebar.file_uploader('Upload your files here', ['png', 'jpg', 'webp'], True)
    _act3_transformations = st.sidebar.multiselect('Select tranformations to apply: ', \
                            ['translate', 'rotate', 'reflect', 'scale', 'shear'])

    if 'translate' in _act3_transformations:
        _act3_translationx = st.sidebar.slider('X Translation', 0, 1000)
        _act3_translationy = st.sidebar.slider('Y Translation', 0, 1000)
        
    if 'reflect' in _act3_transformations:
        _act3_reflection_axis = st.sidebar.radio('Select axis to reflect image along:', ['x', 'y'])
        _act3_reflection = ''
        if _act3_reflectionx and _act3_reflectiony:
            _act3_reflection = 'x y'
        elif _act3_reflectionx:
            _act3_reflection = 'x'
        elif _act3_reflectiony:
            _act3_reflection = 'y'
        
    if 'rotate' in _act3_transformations:
        _act3_rotation = st.sidebar.slider('Rotation', -360, 360, 0)
        
    if 'scale' in _act3_transformations:
        _act3_scale = st.sidebar.slider('Scale', 0.0, 5.0, 1.0, 0.000001)
        
    if 'shear' in _act3_transformations:
        _act3_shearx = st.sidebar.slider('X Shear', 0.0, 5.0, 0.0, 0.000001)
        _act3_sheary = st.sidebar.slider('Y Shear', 0.0, 5.0, 0.0, 0.000001)
        
    st.header("Activity 3")
    st.subheader("Image Transformations")
    for act3_image in _act3_images:
        act3_image = Image.open(act3_image)
        # task3_image = cv2.cvtColor(np.asarray(act3_image), cv2.COLOR_BGR2RGB)
        act3_image = np.asarray(act3_image)
        st.write('Original Image:')
        st.pyplot(act3.visualize(act3_image))
        st.write('Image Transformations: ', *_act3_transformations)
        for transformation in _act3_transformations:
            if transformation == 'translate':
                st.write("Translation")
                st.pyplot(act3.visualize(task3.translate(act3_image, _act3_translationx, _act3_translationy)))
            elif transformation == 'rotate':
                st.write("Rotation")
                st.pyplot(act3.visualize(act3.rotate(act3_image, _act3_rotation)))
            elif transformation == 'reflect':
                st.write("Reflect")
                st.pyplot(act3.visualize(act3.reflect(act3_image, _act3_reflection)))
            elif transformation == 'scale':
                st.write("Scale")
                st.pyplot(act3.visualize(act3.scale(act3_image, _act3_scale)))
            elif transformation == 'shear':
                st.write("Shear")
                st.pyplot(act3.visualize(act3.shear(act3_image, _act3_shearx, _act3_sheary)))

if __name__ == '__main__':
    main()
