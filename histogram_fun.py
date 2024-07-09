import turtle 
from random import randint
import math



def hist_fun (canvas,d) :
    screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle(screen)
    screen.colormode(255)
    #screen.tracer(0)
    t.ht()
    t.speed (5)

    
    data_str = d.get('1.0','end')  # variable to store text box data 
    #print (data_str)
    data_str.strip()

    data = []   # List for data
    height = [] # List of frequency


    j = -1
    for i in range (len(data_str)) :
        if data_str[i] == ',' :
            try :
                data.append(float(data_str[j+1:i]))
                j = i
            except :pass
            
    try :
        data.append(float(data_str[j+1:i+1]))
    except :pass
        

    print (data)

    min_x = min(data)
    max_x = max(data)

    #print (min_value,max_value)

    # Calculations for x axis
    min_X = min_x - min_x % 5
    max_x = max_x+((10-max_x) % 5)

    diff_x = max_x - min_x 

    inc = 1 

    while 1 :
        if diff_x % (5*inc) < 11 :
            break
        inc+=1

    inc *= 5 
    print ('a',inc)
    print ('d',data)
    # Funtion to find frequency
    def bar() :
        temp = inc
        while temp < max_x :
            freq = 0
            for i in data :
                if i <=  temp and i > temp-inc  :
                    freq += 1
            temp += inc 
            if freq != 0 :
                height.append(freq)


    bar ()
    print (height)

    max_height = max(height)

    gcd = math.gcd(*map(int,height))

    if gcd >= max_height/5 :
        diff = gcd 
    else :
        diff = math.ceil(max_height/5)

    print (height)
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

    # Function to draw histrogram 
    def histogram (h) :
        #t.color (random.randint (0,255), random.randint(0,255), random.randint(0,255))
        print (t.xcor())
        t.goto ((t.xcor(), -300))
        t.goto ((t.xcor(), -300 + h*112/diff))
        t.fd (56)

    def labels () :
        #global inc
        t1 = turtle.RawTurtle (screen)
        t1.ht ()
        t1.speed(0)
        t1.up ()

        t1.goto ((-300,-300))
        t1.pencolor ('black')
        t1.left (90)
        for i in range (5) :
            t1.fd (112)
            t1.dot ()
            t1.write ((str(diff*(i+1))),align = 'right')

        t1.goto ((-300,-320))
        t1.right (90)

        temp = int(min_x)
        while 1 :
            if temp <= max_x :
                #t1.fd (56)
                t1.write (str(temp),align = 'center')
                t1.fd (56)
                temp+= inc
            else :
                break
    
    t.up ()
    t.goto ((-300,-300))
    t.down ()

    t.fillcolor ((26,195,237))

    t.begin_fill ()
    for i in height :
        histogram(i)
    t.goto ((t.xcor(),-300))
    t.end_fill ()
    axis()
    labels()

    screen.mainloop()





