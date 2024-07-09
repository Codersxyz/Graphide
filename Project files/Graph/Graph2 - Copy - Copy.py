import turtle
import time
import tkinter as tk

window = tk.Tk()
window.title ("Graphite")
window.geometry('1920x1080')

canvas = tk.Canvas(master=window, width=1000, height=800) #, scrollregion = (1000,1000,-1000,-1000))
canvas.grid(column = 0, row = 0 , columnspan = 200, rowspan = 200)

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
screen.tracer(0,0)
t.hideturtle()

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
    
    screen.reset()
    grid(zoom)
    axis()
    screen.update()

zoom (25)
time.sleep(1)

zoom (50)
time.sleep(1)

zoom (75)
time.sleep(1)

zoom (100)
time.sleep(1)

zoom (50)

screen.mainloop()
    
        
