# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 7 , Number 2

def plus(a, b):
    s = a + b
    return s

def minus(a, b):
    s = a - b
    return s

def multiple(a, b):
    s = a * b
    return s

def division(a, b):
    s = a / b
    return s

a = int(input("첫 번째 수를 입력해주세요. : "))
b = int(input("두 번째 수를 입력해주세요. : "))

for i in range(0, 5):
    menu = str(input("어떤 동작을 수행하시겠습니까? (+,-,*,/) : "))

    if(menu == "+"):
        result = plus(a, b)
        print(result)
    elif(menu == "-"):
        result = minus(a, b)
        print(result)
    elif(menu == "*"):
        result = multiple(a, b)
        print(result)
    elif(menu == "/"):
        result = division(a, b)
        print(result)
    else:
        print("연산자를 정확히 입력해주세요.")

    print("\n")
