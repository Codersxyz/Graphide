from re import A
import turtle 
import random
import math

n = int (input ("Enter numbers of labels : "))

label = []
height = []

for i in range (n) :
    label.append ((input ("Enter label :")))
    height.append (float(input("Enter height :")))

# Function to draw graph 
def bar (height) :
    #t.pencolor ('black')
    t.fd (((360//n)//2)) 
    t.left (90) 
    t.fd (height) 
    t.right (90)
    t.fd ((360//n)//2)
    t.right (90)
    t.fd (height)
    t.left (90)

# Function to draw axis
def axis () :
    t.color ('black')
    t.up ()
    t.goto ((-200,-200))
    t.down ()
    t.fd (400)
    t.stamp()
    t.up ()
    t.goto ((-200,200))
    t.left (90)
    t.stamp ()
    #t.right (90)
    t.down ()
    t.goto ((-200,-200))

# Function to add labels 
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
        t1.fd (((360//n)//2)+((360//n)//2)//2)
        t1.write (i,align = 'center')
        t1.fd (((360//n)//2)//2)

t = turtle.Turtle ()
t.ht ()
turtle.colormode (255)
turtle.tracer (0)

t.up ()
t.goto ((-200,-200))
t.down ()

max_height = max(height)
#min_height = min(height)

gcd = math.gcd(*map(int,height))

if gcd >= max_height/5 :
    diff = gcd 
else :
    diff = math.ceil(max_height/5)
#print (height)

#print (diff)


def draw () :
    for i in height :
        t.color (random.randint (0,255), random.randint(0,255), random.randint (0,255))
        t.begin_fill ()
        bar ((i*72)/diff)
        t.end_fill ()
    # labels (label[i])

    axis ()
    labels ()

draw ()

turtle.update()


turtle.mainloop()

 
