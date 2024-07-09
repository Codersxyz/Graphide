import turtle
import tkinter as tk
import time

sc = turtle.Screen()
sc.screensize(2000,2000)
canvas = sc.getcanvas()

button = tk.Button(canvas.master,text = "+")
canvas.create_window(0,0, window = button)

t = turtle.Turtle()
turtle.tracer(0,0)
t.ht()

# Function to draw line between to specified points
    
def line (x1,y1,x2,y2,color = 'black',wd=1) :
    '''
    Function to draw line between to specified points
        #(x1,y1) are coordinates of start point of line
        #(x2,y2) are coordinates of end point of line
        # color for line color
        # wd for width of line
    '''
    t.ht()
    t.pencolor(color)
    t.width(wd)
    
    t.up()
    t.goto((x1,y1))
    t.down()
    t.goto((x2,y2))

# Function to draw grid

def grid (sp) :
    ''' Function to draw grid
        sp is the spacing between two lines
    '''
    m = 0
    while m < 1000 :
        line (-1000,m,1000,m)
        t.write (str(m))
        line (-1000,-m,1000,-m)
        t.write (str(-m))
        line (m,-1000,m,1000)
        t.write (str(m))
        line (-m,-1000,-m,1000)
        t.write (str(-m))
        m += sp

# Function to draw axis

def axis () :
    '''
        Function to draw axis lines
    '''


    line (-1000,0,1000,0,'blue',1.5)
    line (0,-1000,0,1000,'blue',1.5)
    t.up()
    t.goto((0,0))
    t.down()
    t.pencolor('black')
    t.write('(0,0)')

# Function to zoom in and zoom out

def zoom (zoom) :
    '''
        Function to zoom in and zoom out the canvas
        Argument zoom is for the rate of zoom
    '''
    
    sc.reset()
    grid(zoom)
    axis()
    turtle.update()

zoom (25)
time.sleep(1)

zoom (50)
time.sleep(1)

zoom (75)
time.sleep(1)

zoom (100)
time.sleep(1)

zoom (50)

sc.mainloop()
    
        
