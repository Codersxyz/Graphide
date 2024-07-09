import turtle
import random 
import math

n = int (input ("Enter number : "))

label =  []
height = []

for i in range (n) :
    a = input ("Enter  :") 
    label.append (a)
    height.append (float(input("Enter height : ")))


t = turtle.Turtle()
t.ht ()

turtle.colormode (255)


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

# Function to draw histrogram 
def histogram (height) :
    #t.color (random.randint (0,255), random.randint(0,255), random.randint(0,255))
    print (t.xcor())
    t.goto ((t.xcor(), -200))
    t.goto ((t.xcor(), -200 + height*72/diff))
    t.fd (360//n)
 
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
        t1.fd (((360//n)//2))
        t1.write (i,align = 'center')
        t1.fd (((360//n)//2))

t.fillcolor ((26,195,237))

t.begin_fill ()
for i in height : 
    histogram (i)

t.goto ((t.xcor(),-200))
t.end_fill ()

axis ()
labels()

turtle.mainloop ()


