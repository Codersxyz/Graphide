import turtle 
import random
import math



def bar_graph (canvas,x,y) :
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

    t.up()
    t.goto((-300,-300))
    t.down()

    n = len(x)
    
    label = [i.get() for i in x]
    value = [i.get() for i in y]
    values = [*map(float,value)]

    #print (values)
    max_value = max(values)

    gcd = math.gcd(*map(int,values))

    if gcd >= max_value/10 :
        diff = gcd 
    else :
        diff = math.ceil(max_value/10)

    
    
    # Function to draw graph 
    def bar (height) :
        #t.pencolor ('black')
        t.fd (((560//n))//2)
        t.left (90) 
        t.fd (height) 
        t.right (90)
        t.fd ((560//n)//2)
        t.right (90)
        t.fd (height)
        t.left (90)

    # Function to draw axis
    def axis () :
        t.color ('black')
        t.up ()
        t.goto ((-300,-300))
        t.down ()
        t.fd (600)
        t.stamp()
        t.up ()
        t.goto ((-300,300))
        t.left (90)
        t.stamp ()
        #t.right (90)
        t.down ()
        t.goto ((-300,-300))

    # Function to add labels 
    def labels () :
        
        t1 = turtle.RawTurtle (screen)
        t1.ht ()
        t1.up ()
        t1.goto ((-300,-300))
        t1.pencolor ('black')
        t1.left (90)

        # For y axis
        for i in range (10) :
            t1.fd (56)
            t1.dot ()
            t1.write ((str(diff*(i+1))),align = 'right')

        t1.goto ((-300,-320))
        t1.right (90)
        for i in label :
            t1.fd (((560//n//2)+((560//n)//2)//2))
            t1.write (i,align = 'center')
            t1.fd (((560//n)//2)//2)


    def draw () :
        #global value
        #print ('y')
        for i in values :
            t.color (random.randint (0,255), random.randint(0,255), random.randint (0,255))
            t.begin_fill ()
            print ((i*56)/diff)
            bar ((i*56)/diff)
            t.end_fill ()
        #print ('10')
        axis ()
        labels ()

    draw ()
    screen.update()
    


    
