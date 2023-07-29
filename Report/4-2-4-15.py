# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 4 , Number 15

import turtle

length = int(input("길이 : "))
distance = int(input("간격 : "))

turtle.shape("turtle")

turtle.forward(length + distance * 0)
turtle.up()
turtle.goto(0, -(distance * 1))

turtle.down()
turtle.forward(length + distance * 1)
turtle.up()
turtle.goto(0, -(distance * 2))

turtle.down()
turtle.forward(length + distance * 2)
