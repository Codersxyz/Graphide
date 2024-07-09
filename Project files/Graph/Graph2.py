import turtle
import time
from math import *

sc = turtle.Screen()
sc.screensize(2000,2000)

t = turtle.Turtle()
turtle.tracer(0,0)
t.ht()

# Function to draw line between to specified points
    
def line (x1,y1,x2,y2,color = 'black',wd=1, ) :
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
        #t.write (str(m))
        line (-1000,-m,1000,-m)
        #t.write (str(-m))
        line (m,-1000,m,1000)
        #t.write (str(m))
        line (-m,-1000,-m,1000)
        #t.write (str(-m))
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




def graph1 (sp) :
    pass
    #x = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    #y = [-0.05, -0.05263157894736842, -0.05555555555555555, -0.058823529411764705, -0.0625, -0.06666666666666667, -0.07142857142857142, -0.07692307692307693, -0.08333333333333333, -0.09090909090909091, -0.1, -0.1111111111111111, -0.125, -0.14285714285714285, -0.16666666666666666, -0.2, -0.25, -0.3333333333333333, -0.5, -1.0, math.inf, 1.0, 0.5, 0.3333333333333333, 0.25, 0.2, 0.16666666666666666, 0.14285714285714285, 0.125, 0.1111111111111111, 0.1, 0.09090909090909091, 0.08333333333333333, 0.07692307692307693, 0.07142857142857142, 0.06666666666666667, 0.0625, 0.058823529411764705, 0.05555555555555555, 0.05263157894736842]
    #cnt = -100
    '''
    while cnt < 100:
        
        x.append ((cnt,cnt**2))
        cnt += 0.1
            #print (cnt) 
    '''
    '''except :
            x.append ((1/cnt,cnt))
            cnt += 0.01
            continue
           # cnt = -50
           # while cnt < 0 :
             #   cnt += 0.1
              #  x.append ((1/cnt,cnt))
    cnt = 0.01
    while cnt < 51 :
        x.append ((1/cnt,cnt))
        cnt += 0.01
    '''    
            
    #while cnt < 50 :
            #pass
    #print (x)
        
    t.pencolor('red')
    #t.up ()
    # for i in x :
    #    y.append ((i[0]*sp,i[1]*sp))
        

    '''for i in x :
        if i != (0,0) :
            y.append ((i[0]*sp/2,i[1]*sp/2))
        else :
            y.append ((0,0))
    #print (y)
    y.sort()
    #t.up()'''
    t.down()
    for i in range (40):
        t.goto ((x[i]*sp,y[i]*sp))
        t.dot ()
        #if (i == (5*sp,25*sp)) :
           # t.write("a")
        #t.dot()


def graph (sp) :
    global cnt
    cnt = 0
    t.pencolor ('red')
    t.up()
    try :
        t.goto((-20*sp,(eval(eq.replace('x','('+str(-20)+')')))*sp))
        x = -20
    except :
        t.goto((0.0025*sp,(eval(eq.replace('x','('+str(0.0025)+')')))*sp))
        x = 0.0025

    t.down()
    while x < 21 :
        try :
            #t.down()
            x +=0.0025
            y = eval(eq.replace('x','('+str(x)+')'))
            
            if abs(t.ycor() - y*sp) > 500 :
                t.up ()
                x += 0.0025
                t.goto ((x*sp,(eval(eq.replace('x','('+str(x)+')')))*sp))
                t.down ()

            #print (y)
            t.goto ((x*sp,y*sp))
            #t.dot()
            #t.down()
        except :
            #x+=0.0025
            #t.up()
            #t.goto ((x+0.0025*sp,(eq.replace('x','('+str(x+0.0025)+')')*sp)))
            #t.down()
            #t.up ()
            pass
        #t.dot()    

# Function to zoom in and zoom out

def zoom (zoom) :
    '''
        Function to zoom in and zoom out the canvas
        Argument zoom is for the rate of zoom
    '''
    
    sc.reset()
    grid(zoom)
    axis()
    graph (zoom)
    turtle.update()




eq =  input ("Enter the equation : ")
zoom (50)
#print (cnt)



#zoom (100)
#time.sleep(1)

#zoom (75)
#time.sleep(1)
'''
zoom (100)
time.sleep(1)

zoom (50)
#graph ()'''

sc.mainloop()
    
        
