import turtle 
import random 
import math 

def line_graph (canvas,l,d) :
    # d is 2d list of all values entries
    # l is list of labels

    label = [i.get() for i in l]
    
    value = [[i.get() for i in j] for j in d]
    data = []
    for i in range (3) :
        try :
            data.append([*map(float,value[i])])
        except : pass
   

    n = len(data[0])

    # Max value in data
    max_value = data[0][0]
    for i in data :
        for j in i :
            if j > max_value :
                max_value = j  

    print (max_value)
    gcd = math.gcd(*map(int,data[0]))       # GCD of the data

    if gcd >= max_value/10 :
        diff = gcd 
    else :
        diff = math.ceil(max_value/10)


    # creating turtle objects 

    screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle (screen)
    t.ht ()
    screen.tracer (0,0)
    screen.colormode (255)

    # Function to draw axis

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

    def axis () :
        '''
            Function to draw axis lines
        '''

        line (-300,-300,300,-300)
        t.stamp ()
        line (-300,-300,-300,300)
        t.left (90)
        t.stamp ()

    def labels () :
    
        t1 = turtle.RawTurtle (screen)
        t1.ht ()
        t1.up ()

        t1.goto ((-300,-300))
        t1.pencolor ('black')
        t1.left (90)
        for i in range (10) :
            t1.fd (56)
            t1.dot ()
            t1.write ((str(diff*(i+1))),align = 'right')

        t1.goto ((-300,-320))
        t1.right (90)

        for i in label :
            t1.fd (((560//n)))
            t1.write (i,align = 'center')

    def line_graph () :
        t.width (2)

        #t.right (90)
        for i in data :
            t.up ()
            t.goto ((-300,-300))
            t.down()
            t.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            #t.left (90)
            #
            #t.dot ()
            #t.up()
            #t.fd (360/n)
            #t.goto ((t.xcor(),(i[0]*72/diff-200)))
            try :
                for j in i :
                    #print (j)
                    if j ==  i[0] :
                        t.up ()
                        t.goto ((t.xcor()+560/n,(j)*56/diff-300))
                        t.down ()
                        #t.dot ()
                    else :
                        t.goto ((t.xcor()+560/n,(j)*56/diff-300))
                    #t.fd (360/n)
                    #t.fd(j*36/diff)
                    t.dot ()
            except :pass
    axis ()
    line_graph ()
    labels ()

    screen.mainloop()