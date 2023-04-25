import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
#st.set_option ('browser.gatherUsageStats' , False)




def DDALine(x1, y1, x2, y2, color):
    fig = plt.figure()

    dx = x2 - x1
    dy = y2 - y1

    x, y = x1, y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xinc = float(dx / steps)
    yinc = float(dy / steps)

    for i in range (0, steps + 1):
        plt.plot(round(x1), round(y1), color, marker='s', markersize=5) # marker='s', markersize=5
        # if(i == round(steps+1)):
        #     plt.plot(round(x1), round(y1), color, marker='o', markersize=25) # marker='0', markersize=25
        x1 += xinc
        y1 += yinc
    # plt.xlim(0, 100)
    # plt.ylim(0, 100)
    plt.plot(round((x1 + x)/2), round((y1 + y)/2), 'bo', markersize=5)
    
    return fig

def bresenham(x1,y1,x2,y2, color):
    fig = plt.figure()

    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    # print(f"x = {x}, y = {y}")
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        # print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates, color, marker='s', markersize=5)
    plt.plot(round(dx/2 + x1), round(dy/2 + y1), 'bo', markersize=5)

    return fig

def midpoint(x1, y1, x2, y2, color):
    fig = plt.figure()

    dx = x2 - x1
    dy = y2 - y1

    # Initialize the decision parameter
    d  = dy - (dx/2)
    x = x1
    y = y1

    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    while (x<x2):
        x = x + 1
        # East is Chosen
        if (d<0):
            d = d + dy

        # North East is Chosen
        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
        # print(f"x = {x}, y = {y}")
    plt.plot(xcoordinates, ycoordinates, color, marker='s', markersize=5)

    return fig

def main():
    x = int(input("Enter x1: "))
    y = int(input("Enter y1: "))
    x_end = int(input("Enter x2: "))
    y_end = int(input("Enter y2: "))
    color = "#aa2533"
    fig = DDALine(x, y, x_end, y_end, color)
    plt.show()
    bresenham(x, y, x_end, y_end, color)
    midpoint(x, y, x_end, y_end, color)
    
        st.title("Midterm Exam in CCS221")

    st.sidebar.header("Line Algorithm Parameters")
    _act1_x0, _act1_y0, _act1_x1, _act1_y1 = st.sidebar.slider('Starting X', 1, 100), \
                     st.sidebar.slider('Starting Y', 1, 100), \
                     st.sidebar.slider('Ending X', 1, 100, 10), \
                     st.sidebar.slider('Ending Y', 1, 100, 10)
    
    st.header("Activity 1")
    st.subheader("DDA Line Algorithm")
    st.pyplot(act1.DDALine(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Bresenham's Line Algorithm")
    st.pyplot(act1.bresenham(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Midpoint Line Algorithm")
    st.pyplot(act1.midpoint(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))

if __name__ == "__main__":
    main()
