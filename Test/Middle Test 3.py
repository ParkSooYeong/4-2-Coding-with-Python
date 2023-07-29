# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Middle Test 3

# 가로, 세로를 입력받고 그걸 매개변수로 사용하여 터틀 그래픽으로 사각형 그리기
# 사각형을 그리는 rectangle_draw 함수와 넓이를 구하는 rectangle_area 함수
# 호출하고 선언 및 그려진 사각형 아래에 가로,세로,넓이가 표시될 것

import turtle

def rectangle_draw(a,b):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.penup()
    turtle.forward(50)
    turtle.write("가로          세로          인 사각형의 넓이 = ")
    turtle.goto(25,-50)
    turtle.write(a)
    turtle.goto(75,-50)
    turtle.write(b)
    turtle.goto(200,-50)
    turtle.write(rectangle_area(a,b))
    turtle.goto(0,-60)

def rectangle_area(c,d):
    s = c * d
    return s

length = int(input("가로 : "))
height = int(input("세로 : "))

result = rectangle_area(length, height)

print("넓이 :", result)

rectangle_draw(length, height)
