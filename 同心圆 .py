import turtle
turtle.setup(1400,900)
turtle.pensize(6)
turtle.pencolor(0.20,0.90,0.91)
r=0
for i in range(9):
    r=r+20
    turtle.circle(r,360)
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(20)
    turtle.pendown()
    turtle.seth(0)

    


