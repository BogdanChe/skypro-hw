import turtle

turtle.shape("turtle")

turtle.speed(1000)

radius=10
turtle.left(90)

for i in range(10):
    turtle.circle(radius)
    turtle.circle(-radius)
    radius +=10

turtle.exitonclick()