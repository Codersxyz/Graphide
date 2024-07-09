import turtle 
import random



def pie_chart (canvas,x,y) :
    '''
        Function to create bar graph
        x is list of label_entries
        y is list of value_entries
    '''
    #global screen,t,n
    #global label,value,diff
    

    screen = turtle.TurtleScreen(canvas)
    screen.reset()
    t = turtle.RawTurtle(screen)

    screen.tracer(0,0)
    screen.colormode(255)
    t.ht()
    t.speed (0)

    t.goto ((0,-250))

    t1 = turtle.RawTurtle(screen)
    t1.up ()
    t1.ht ()
    t1.right (90)

    n = len(x)
    
    label = [i.get() for i in x]
    value = [i.get() for i in y]
    percent = [*map(float,value)]

    total = sum(percent)

    def labels () :
        #pass
        t1.left (angle/2)

        if (angle) > 30 :
            t1.fd (170)
        else :
            t1.fd (270)

        #t1.pencolor ('black')
        t1.write (label[i],align = 'center', font = ('Arial', 11,'normal'))
        t1.goto ((0,0))
        t1.left (angle/2)

    for i in range (n) :
        angle = ((percent[i]/total)*360)
        t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        t.begin_fill ()
        t.circle(250, extent = (angle))
        pos = t.pos ()
        labels()
        t.goto ((0,0))
        t.end_fill ()
        t.goto (pos)
    

    '''
    t.up ()
    t.pencolor ('black')

    t.left (((percent[i]/total)*360)//2)
    for i in range (n) :
        t.left (((percent[i]/total)*360)//2)
        t.fd (220)
        t.write (label[i],align = 'left', font = ('Arial', 16,'normal'))
        t.goto (0,0)
        t.left (((percent[i]/total)*360)//2)
        
    '''
    screen.update ()

