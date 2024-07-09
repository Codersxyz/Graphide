import turtle 
import random 
import math 

m = int (input("Enter number of sets of points :"))
n = int (input ("Enter number of points : "))

data =  [[0 for i in range (n)]for j in range (m)]
print (data)
label = []
#points = []

for i in range (m) :
    for j in range (n) :
        if j == 0 :
            a = input ("Enter  :") 
            label.append (a)
        data[i][j] =  (float(input("Enter value : ")))
    #print (points)
    #print (data)
    #points.clear()


#label = set(label)

max_y = max(data[0])

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

def grid () :
    ''' Function to draw grid
        sp is the spacing between two lines
    '''
    sp = 72
    m = 0 
    while m < 360 :
        line (-200,m,175,m,'grey',0.5)
        #t.write (str(m))
        line (-200,-m,175,-m,'grey',0.5)
        #t.write (str(-m))
        line (m,-200,m,175,'grey',0.5)
        #t.write (str(m))
        line (-m,-200,-m,175,'grey',0.5)
        #t.write (str(-m))
        m += sp
    

# Function to draw axis

def axis () :
    '''
        Function to draw axis lines
    '''

    line (-200,-200,200,-200)
    t.stamp ()
    line (-200,-200,-200,200)
    t.left (90)
    t.stamp ()

    #t.up()
    #t.goto((0,0))
    #t.down()
    #t.pencolor('black')
    #t.write('(0,0)')

#min_height = min(height)

gcd = math.gcd(*map(int,data[0]))

if gcd >= max_y/5 :
    diff = gcd 
else :
    diff = math.ceil(max_y/5)

def labels () :
    
    t1 = turtle.Turtle ()
    t1.ht ()
    t1.up ()

    t1.goto ((-200,-200))
    t1.pencolor ('black')
    t1.left (90)
    for i in range (5) :
        t1.fd (72)
        t1.dot ()
        t1.write ((str(diff*(i+1))),align = 'right')

    t1.goto ((-200,-220))
    t1.right (90)

    for i in label :
        t1.fd (((360//n)))
        t1.write (i,align = 'center')
        #t1.fd (((360//n)//2))


t = turtle.Turtle ()
t.ht ()
#turtle.tracer (0)
turtle.colormode (255)

def line_graph () :
    t.width (1.4)

    #t.right (90)
    for i in data :
        t.up ()
        t.goto ((-200,-200))
        t.down()
        t.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        #t.left (90)
        #
        #t.dot ()
        #t.up()
        #t.fd (360/n)
        #t.goto ((t.xcor(),(i[0]*72/diff-200)))
        for j in i :
            #print (j)
            if j ==  i[0] :
                t.up ()
                t.goto ((t.xcor()+360/n,(j)*72/diff-200))
                t.down ()
                #t.dot ()
            else :
                t.goto ((t.xcor()+360/n,(j)*72/diff-200))
            #t.fd (360/n)
            #t.fd(j*36/diff)
            t.dot ()


#grid ()
axis ()
line_graph ()
labels ()
#turtle.update()

turtle.mainloop ()