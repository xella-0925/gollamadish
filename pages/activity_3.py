import cv2
import numpy as np
import matplotlib.pyplot as plt

def translated_img(img, x, y):

    m_translation = np.float32([[1, 0, x],
                     [0, 1, y]])
    translated_img = cv2.warpAffine(img, m_translation, (img.shape[1], img.shape[0]))
    return translated_img

def rotated_img(img, θ):
 
    m_rotation = cv2.getRotationMatrix2D((img.shape[1] // 2, img.shape[0] // 2), θ, 1.0)
    rotated_img = cv2.warpAffine(img, m_rotation, (img.shape[1], img.shape[0]))
    return rotated_img

def scaled_img(img, scale):

    m_scaled = np.float32([[scale, 0, 0],
                    [0, scale, 0]])
    scaled_img = cv2.warpAffine(img, m_scaled, (img.shape[1], img.shape[0]))
    return scaled_imgm_scaled

def sheared_img(img, x, y):
    
    m_sheared = np.float32([[1, x, 0],
                    [y, 1, 0]])
    sheared_img = cv2.warpAffine(img, m_sheared, (img.shape[1], img.shape[0]))
    return sheared_img

def reflected_img(img, axis):

    if 'x' in axis.lower():
        reflected_img = cv2.flip(img, 1)
    if 'y' in axis.lower():
        reflected_img = cv2.flip(img, 0)
    return reflected_img

def visualize(img):
    fig = plt.figure()
    plt.imshow(img)
    plt.axis('off')
    return fig

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
    
    for img in images:
        print('Original Image')
        visualize(img)
        if 'translate' in transformations.lower():
            print('Translated Image')
            visualize(translated_img(img, int(input('Enter x translation: ')), int(input('Enter y translation: '))))
        if 'rotate' in transformations.lower():
            print('Rotated Image')
            visualize(rotated_img(img, float(input('Enter rotation angle: '))))
        if 'scale' in transformations.lower():
            print('Scaled Image')
            visualize(scaled_img(img, float(input('Enter scale factor: '))))
        if 'shear' in transformations.lower():
            print('Sheared Image')
            visualize(sheared_img(img, float(input('Enter x shear factor: ')), float(input('Enter y shear factor: '))))
        if 'reflect' in transformations.lower():
            print('Reflected Image')
            visualize(reflected_img(img, input('Enter axis to reflect image along: ')))
            
def main():
    # img = cv2.imread('images/img1.webp')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # visualize(img)
    
    # # Translate the image 100 pixels to the right and 50 pixels down
    # translated = translate(img, 100, 50)
    # visualize(translated)
    
    # # Rotate the image 45 degrees counter-clockwise
    # rotated = rotate(img, 45)
    # visualize(rotated)
    
    # # Scale the image by 50%
    # scaled = scale(img, 0.5)
    # visualize(scaled)
    
    # # Shear the image by 0.2 horizontally and 0.3 vertically
    # sheared = shear(img, 0.2, 0)
    # visualize(sheared)
    
    # # Reflect the image along the x-axis
    # reflected = reflect(img, 'x y')
    # visualize(reflected)

    imgs = multiple_image_load()
    images_transform(*imgs)

if __name__ == '__main__':
    main()
