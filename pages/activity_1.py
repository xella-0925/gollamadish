import matplotlib.pyplot as plt
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def DDALine (x1, y1, x2, y2, color):
    fig = plt.figure()
    dx = x2 -x1
    dy = y2 -y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float (dx / steps)
    Yinc = float (dx / steps)

    for i in range(0, int(steps +1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    
    return fig

def bresenham(x1, y1, x2, y2, color):
    fig = plt.figure()
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)
 
    y2 = y1
    for x1 in range(x1, x2+1):
        slope_error_new = slope_error_new + m_new

        if (slope_error_new >= 0):
          
            x1 += 1
            y1 += 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)
    plt.plot(int(x1), int(y1), color, marker = 's', markersize = 5)
    
    return fig

def midpoint(x1, y1, x2, y2):
    fig = plt.figure()
    dx = x2 - x1
    dy = y2 - y1

    d  = dy - (dx/2)
    x = x1
    y = y1

   #print(f"x = {x}, y = {y}")
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
        print(f"x = {x}, y = {y}")
    plt.plot(xcoordinates, ycoordinates)
    return fig

def main ():

    plt.title("DDA Line Algorithm")
x=int(input("Enter X1:"))
y=int(input("Enter Y1:"))
xEnd= int(input("Enter X2:"))
yEnd = int(input("Enter Y2:"))
color = "r."

fig = DDALine(x, y, xEnd, yEnd, color)
plt.show()

#print("Bresenham Line Algorithm")
plt.title("Bresenham Line Algorithm")
x1 = int(input("Enter X1: "))
y1 = int(input("Enter Y1: "))
x2 = int(input("Enter X2: "))
y2 = int(input("Enter Y2: "))
color = "r"

bresenham(x1, y1, x2, y2, color)

#print("Midpoint Line Algorithm")
plt.title("Midpoint Line Algorithm")
x1 = int(input("Enter X1: "))
y1 = int(input("Enter Y1: "))
x2 = int(input("Enter X2: "))
y2 = int(input("Enter Y2: "))
color = "b"

midpoint(x1, y1, x2, y2)
    
if __name__=='__main__':
    main()
