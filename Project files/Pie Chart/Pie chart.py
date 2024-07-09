import turtle 
import random 

n = int (input ("Enter number : "))

label =  []
percent = []

for i in range (n) :
    a = input ("Enter  :") 
    label.append (a)
    percent.append (float(input("Enter percent : ")))


total = sum(percent)
t =  turtle.Turtle () 
turtle.tracer (0)
turtle.colormode (255)
t.ht()

t.goto ((0,-200))

t1 = turtle.Turtle ()
t1.up ()
t1.ht ()
t1.right (90)


def labels () :
    #pass
    t1.left (angle/2)

    if (angle) > 30 :
        t1.fd (120)
    else :
        t1.fd (220)

    #t1.pencolor ('black')
    t1.write (label[i],align = 'center', font = ('Arial', 11,'normal'))
    t1.goto ((0,0))
    t1.left (angle/2)

for i in range (n) :
    angle = ((percent[i]/total)*360)
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.begin_fill ()
    t.circle(200, extent = (angle))
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
turtle.update ()


turtle.mainloop()

    




    
