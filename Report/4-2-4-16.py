# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 4 , Number 16

import turtle

radius = int(input("반지름 : "))

turtle.shape("turtle")

turtle.circle(radius)
turtle.up()
turtle.goto(0, radius * 2)
turtle.down()
turtle.circle(radius / 2)
