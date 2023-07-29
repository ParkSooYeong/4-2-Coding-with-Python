# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Middle Test 2

# 두 수와 연산자를 입력받아 연산자에 맞는 동작을 하는 함수 calc 선언하고 호출
# 잘못된 연산자를 입력할 시, "잘못된 형식입니다" 메시지를 출력

def calc(num1, num2, op):
    if op == '+':
        s = num1 + num2
    elif op == '-':
        s = num1 - num2
    elif op == '*':
        s = num1 * num2
    elif op == '/':
        s = num1 / num2
    else:
        s = str("잘못된 형식입니다.")
    return s

number1 = int(input("숫자 1 : "))
number2 = int(input("숫자 2 : "))
operator = str(input("연산자 : "))

result = calc(number1, number2, operator)

print("두 수의 연산 결과 :", result)
