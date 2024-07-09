import turtle
import time
import tkinter as tk
from math import*

def raw (canvas,left_frame,entries,right_frame) :

    canvas.delete('all')
    screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle(screen)
    screen.tracer(0,0)
    t.hideturtle()
    t.speed (0)

    global z # zoom percent
    z = 50

    global color 
    color = ['red','green','yellow','blue','orange']
    # Function to draw line between to specified points
    
    def line (x1,y1,x2,y2,color = '#c6c6c6',wd=1) :
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


        line (-1000,0,1000,0,'black',1.5)
        line (0,-1000,0,1000,'black',1.5)
        t.up()
        t.goto((0,0))
        t.down()
        t.pencolor('black')
        t.write('(0,0)')

    def graph (sp,eq,color) :
        '''
            Function to draw graph
        '''
        #eq = str(eq)
        t.pencolor (color)
        t.up()
        try :
            t.goto((-25*sp,(eval(eq.replace('x','('+str(-25)+')')))*sp))
            x = -25
        except :
            t.goto((0.0025*sp,(eval(eq.replace('x','('+str(0.0025)+')')))*sp))
            x = 0.0025

        t.down()
        while x < 26 :
            try :
                x +=0.0025
                y = eval(eq.replace('x','('+str(x)+')'))
                
                if abs(t.ycor() - y*sp) > 500 :
                    t.up ()
                    x += 0.0025
                    t.goto ((x*sp,(eval(eq.replace('x','('+str(x)+')')))*sp))
                    t.down ()
                t.goto ((x*sp,y*sp))

            except :
                pass
        screen.update()

    # Function to zoom in and zoom out

    def zoom (r) :
        '''
            Function to zoom in and zoom out the canvas
            Argument zoom is for the rate of zoom
        '''
        global color
       # color = []

        screen.reset()
        grid(r)
        axis()
        for i in range (len(entries)) :
            try :
                graph(z,entries[i].get(),color[i])
            except :
                pass
        #screen.update()
        screen.update()

    # Function to zoom in graph
    def zoom_in_fun() :

        global z 
        if z < 100 :
            z+=25
            zoom (z)

    # Function to zoom out in graph
    def zoom_out_fun() :
        global z 
        if z > 25 :
            z-=25
            zoom (z)


    def plot_graph() :
        #print (entries)
        global z
        global color
        for i in range (len(entries)) :
            try :
                graph(z,entries[i].get(),color[i])
            except :
                pass

    plot = tk.Button(master=left_frame,text='Plot',width=49,height=3,border=0.5,command=lambda:plot_graph())    
    plot.grid(row=7,column=0,columnspan=2,sticky='s',pady=2)

    zoom_in = tk.Button (master=right_frame,text='+',font=('calibre',10,'normal'),width=4,height=2,command=lambda:zoom_in_fun())
    zoom_in.grid(row=4,column=0,sticky='nw')

    zoom_out =  tk.Button (master=right_frame,text='-',font=('calibre',10,'normal'),width=4,height=2,command=lambda:zoom_out_fun())
    zoom_out.grid(row=5,column=0,sticky='nw')
    
    zoom (z)

    screen.mainloop()

