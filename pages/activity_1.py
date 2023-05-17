import matplotlib.pyplot as plt
import streamlit as st

st.title("Activity 1")

def DDALine(x1, y1, x2, y2, color):
    fig = plt.figure()
    
    #Calculates the differences in x and y coordinates (dx and dy).
    dx = x2 - x1
    dy = y2 - y1
    
    #Initializes the starting coordinates (x and y) with x1 and y1.
    x, y = x1, y1
    
    #Determines the number of steps needed to draw the line based on the larger difference between dx and dy (absolute values).
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    #Calculates the increments (xinc and yinc) to move along the line based on the steps.
    xinc = float(dx / steps)
    yinc = float(dy / steps)
    
    #Iterates over the number of steps and plots each point along the line.
    for i in range (0, steps + 1):
        plt.plot(round(x1), round(y1), color, marker='s', markersize=5) # marker='s', markersize=5
     
        x1 += xinc
        y1 += yinc

    # Plot a blue circle marker at the midpoint of the line
    plt.plot(round((x1 + x)/2), round((y1 + y)/2), 'bo', markersize=5)
    
    return fig

def bresenham(x1,y1,x2,y2, color):
    fig = plt.figure()
    
    # Calculates differences in coordinates
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = dy/float(dx)

    # Adjust coordinates for steep lines
    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    # Initialize Bresenham algorithm variables
    p = 2*dy - dx

    xcoordinates = [x]
    ycoordinates = [y]
    
    # Iterates and calculates next points using Bresenham's algorithm
    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        xcoordinates.append(x)
        ycoordinates.append(y)

    # Plots the line using the calculated coordinates
    plt.plot(xcoordinates, ycoordinates, color, marker='s', markersize=5)
    plt.plot(round(dx/2 + x1), round(dy/2 + y1), 'bo', markersize=5)

    return fig

def midpoint(x1, y1, x2, y2, color):
    fig = plt.figure()

    dx = x2 - x1
    dy = y2 - y1

    d  = dy - (dx/2)
    x = x1
    y = y1

    xcoordinates = [x]
    ycoordinates = [y]

    while (x<x2):
        x = x + 1

        if (d<0):
            d = d + dy

        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
    plt.plot(xcoordinates, ycoordinates, color, marker='s', markersize=5)

    return fig

def main():
    st.sidebar.header("Line Algorithm Parameters")
    x = st.sidebar.slider("x1", 0, 100, 50)
    y = st.sidebar.slider("y1", 0, 100, 50)
    x_end = st.sidebar.slider("x2", 0, 100, 75)
    y_end = st.sidebar.slider("y2", 0, 100, 75)
    color = "#aa2533"
    
    # Performs line drawing using DDA Line algortithm
    fig_dda = DDALine(x, y, x_end, y_end, color)
    st.subheader("DDA Line Algorithm")
    st.pyplot(fig_dda)
    
    # Performs line drawing using Bresenham Line algortithm
    fig_bresenham = bresenham(x, y, x_end, y_end, color)
    st.subheader("Bresenham's Line Algorithm")
    st.pyplot(fig_bresenham)
    
    # Performs line drawing using Midpoint Line algortithm
    fig_midpoint = midpoint(x, y, x_end, y_end, color)
    st.subheader("Midpoint Line Algorithm")
    st.pyplot(fig_midpoint)

        
if __name__ == "__main__":
    main()
