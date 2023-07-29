# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Week 11 , Number 5

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(N, M): # Solution 함수 작성

    total = 0

    for i in range(N, M + 1):
        
        if i % 2 == 0:

            total += i * i

    return total

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
N = 4
M = 7
ret = solution(N, M)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution 함수의 반환 값은", ret, "입니다.")
