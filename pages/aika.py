import numpy as np
import cv2
import matplotlib.pyplot as plt

img_ = cv2.imread("jen.jpg")
img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

rows, cols, dims = img_.shape

def translate (img_, rows, cols):
    m_translation_ = np.float32 ([[1, 0, 100],
                                  [0, 1, 50],
                                  [0, 0, 1]])
                                  
    translated_img_ = cv2.warpPerspective(img_, m_translation_, (cols, rows))

    return translated_img_

translated_img_ = translate (img_, rows, cols)
plt.axis('off')
plt.imshow(translated_img_)