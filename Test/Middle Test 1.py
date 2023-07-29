# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Middle Test 1

# 매개변수를 받아 양수면 1, 음수면 -1을 반환하는 pzn 함수를 선언하고 호출
# 입력한 수가 양수(0 포함)이면 "양수"를, 음수이면 "음수"를 출력

def pzn(num):
    if num >= 0:
        r = 1
    elif num < 0:
        r = -1
    return r

number = int(input("숫자 : "))

result = pzn(number)

if result == 1:
    print("양수")
elif result == -1:
    print("음수")
