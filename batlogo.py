import turtle
s=turtle.getscreen()
turtle.Screen().bgcolor("black")
turtle.ht()
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t1.penup()
t2.penup()
t1.goto(0,-300)
t2.goto(0,-300)
t3.goto(-30,-300)
t1.pendown()
t2.pendown()
t1.left(90)
t2.left(90)
t3.left(90)
t1.width(4)
t2.width(4)
t1.pencolor("red")
t2.pencolor("red")
t1.circle(300,extent=90)
t2.circle(-300,extent=90)
t1.right(100)
t2.left(100)
t1.circle(125,extent=100)
t2.circle(-125,extent=100)
t1.backward(310)
t2.backward(310)
t1.left(95)
t2.right(95)
t3.fillcolor("black")
t3.speed(10)
t3.begin_fill()
t3.fd(25)
t3.left(90)
t3.backward(80)
t3.lt(90)
t3.fd(100)
t3.lt(90)
t3.backward(80)
t3.end_fill()
t3.hideturtle()
t1.circle(90,extent=75)
t2.circle(-90,extent=75)
t1.left(100)
t2.right(100)
t1.forward(60)
t2.forward(60)
t1.right(150)
t2.left(150)
t1.forward(30)
t2.forward(30)
t1.left(100)
t1.circle(-40,extent=76)
t1.ht()
t2.ht()
turtle.exitonclick()
