import turtle

t = turtle.Turtle()
t.ht()
turtle.tracer (0,0)

t.width(0.5)
t.color("grey")

x = [(40,100),(100,150),(200,200),(250,250),(300,300)]

for i in range (-500,500,25) :
    t.up()
    t.goto((-500,i))
    t.down()
    t.forward (1000)


for i in range (-500,500,10) :
    t.up()
    t.goto((i,-500))
    t.right(90)
    t.down()
    t.forward (1000)

t.width (1.25)
t.pencolor("blue")

t.up()
t.goto ((-500,0))
t.down()
t.forward (1000)

t.up()
t.goto ((0,500))
t.down()
t.goto ((0,-500))

turtle.update()

t.up()
t.goto ((0,0))
t.pencolor('black')
t.write ("(0,0)",)


t.pencolor ('black')
t.width (2)
for i in x :
    t.goto((i[0],0))
    t.write(str('('+str(i[0]))+',0)')
    t.down()
    t.left (90)
    t.forward(4)
    t.right(90)
    t.up()
    
    t.goto((0,i[1]))
    t.write('(0,'+str(i[1])+')')
    t.down()
    t.forward(4)
    t.up()

t.pencolor("red")
t.width (1)

for i in x :
    t.goto(i)
    t.down()
    t.dot()

print (max(x))
    

turtle.update()

turtle.mainloop
