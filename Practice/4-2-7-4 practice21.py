# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 7 , Number 4

import turtle
import math

def Triangle_draw(a, b):                # 해당 함수는 각도를 120도로 고정시켜놓았기 때문에
    turtle.forward(a)                   # 밑변과 높이를 매개변수로 받은 후,
    turtle.left(120)                    # 피타고라스 정리에 의한 빗변의 길이로 그려짐.
    turtle.forward(math.sqrt(a*a + b*b))
    turtle.write(math.sqrt(a*a + b*b))
    turtle.left(120)
    turtle.forward(math.sqrt(a*a + b*b))
    turtle.write(math.sqrt(a*a + b*b))
    turtle.left(120)
    turtle.forward(a)

def Triangle_area(a, b):
    area = (a * b) / 2
    return area

base = int(input("삼각형의 밑변을 입력해주세요. : "))
height = int(input("삼각형의 높이를 입력해주세요. : "))

result = Triangle_area(base, height)

print("삼각형의 넓이는", result, "입니다.")

Triangle_draw(base, height)
