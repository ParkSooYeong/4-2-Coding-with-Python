# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Week 3 , Number 3

# Problem 1 : 반지름을 입력받아서 원의 넓이를 구하고 그래픽을 이용해서 표현하시오.
# Problem 2 : 가로와 세로를 입력받아서 사각형의 넓이를 구하고 그래픽을 이용해서 표현하시오.

# 주의사항 : 모든 내용은 그래픽 창에 표현이 되어야한다. (write 함수)

import turtle
import math

rad = int(input("문제 1. 반지름을 입력하세요.(cm) : "))

cir = rad * rad * math.pi

turtle.circle(rad)
turtle.write(cir)

print("원의 넓이는 ", cir, " cm^2 입니다.")
print("")

row = int(input("문제 2. 사각형의 가로 길이를 입력하세요.(cm) : "))
col = int(input("문제 2. 사각형의 세로 길이를 입력하세요.(cm) : "))

squ = row * col

turtle.reset()
turtle.forward(row)
turtle.left(90)
turtle.forward(col)
turtle.left(90)
turtle.forward(row)
turtle.left(90)
turtle.forward(col)
turtle.write(squ)

print("사각형의 넓이는 ", squ, " cm^2 입니다.")
