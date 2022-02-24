import turtle
t = turtle.turtles()
s = turtle.Screen()
s.bgcolor('black')
turtle.speed(11)
col=['orange', 'purple', 'gray', 'yellow']
c=0
#apran_khunger
for i in range(50):
    turtle.forward(i*10)
    turtle.right(144)
    turtle.pen(fillcolor="black", pencolor="violet", pensize=1)
    turtle.fillcolor("violet")
    turtle.color(col[c])
    if c==3:
        c=0
    else:
        c+=1
