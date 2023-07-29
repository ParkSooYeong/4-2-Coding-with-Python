# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 7 , Number 3

def pzn(num):
    if(num % 2 == 0):
        rest = 0
    elif(num % 2 == 1):
        rest = 1
    return rest

number = int(input("숫자를 입력해주세요. : "))

result = pzn(number)

if(result == 0):
    print("짝수입니다.")
elif(result == 1):
    print("홀수입니다.")
