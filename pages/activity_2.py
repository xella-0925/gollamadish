import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[1, 0, 1]
                   , [0, 0, 0]
                   , [1, 0, 1]])

def fill(x, y, color):
    
    fig = plt.figure()
    for i in range(len(two_d_ar,r)):
        for j in range(len(two_d_arr)):
            two_d_arr[x][y] = color

    img = plt.imshow(two_d_arr, cmap='rainbow', interpolation='none')
    img.set_clim([0, 100])
    plt.colorbar()
    
    return fig

def main():
    fill(2, 1, 85)
    
if __name__=="__main__":
    main()