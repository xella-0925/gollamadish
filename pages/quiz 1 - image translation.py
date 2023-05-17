import numpy as np
import cv2
import streamlit as st

# Defines the translation matrix
def translate(img_, rows, cols, Bx, By):
    translated_img_ = np.float32(([1, 0, Bx],
                                 [0, 1, By],
                                 [0, 0, 1]))

    translated_img_ = cv2.warpPerspective(img_, translated_img_, (cols, rows))

    return translated_img_ 

# Streamlit app
st.title("Quiz 1 - Translation")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Sidebar file uploader widget
st.sidebar.header("Image Translation (Old - New)")
uploaded_file = st.sidebar.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Reads and process the uploaded image
    img_ = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    rows, cols, dims = img_.shape

    # Gets user input for the translation parameters
    Bx_old = st.sidebar.number_input("Bx_old:", min_value=0, max_value=cols-1, step=1, value=0)
    By_old = st.sidebar.number_input("By_old:", min_value=0, max_value=rows-1, step=1, value=0)

    Tx = st.sidebar.number_input("Tx:", min_value=-cols, max_value=cols, step=1, value=0)
    Ty = st.sidebar.number_input("Ty:", min_value=-rows, max_value=rows, step=1, value=0)

    no_of_imgs = st.sidebar.slider("Number of Images:", min_value=1, max_value=10, value=1, step=1)

    # Initialize the new translation coordinates
    Bx_new = Bx_old
    By_new = By_old
    
    # Displays the original image
    st.image(img_, caption="Original Image", use_column_width=True)
    
    # Performs translation and display new images
    for no_of_tests in range(no_of_imgs):
       # Translates the image using the specified parameters
       new_img = translate(img_, rows, cols, Bx_new, By_new)
    # Displays the new image
       st.image(new_img, caption=f"New Image {no_of_tests+1}", use_column_width=True)
       # Updates the translation coordinates for the next iteration
       Bx_new += Tx
       By_new += Ty
