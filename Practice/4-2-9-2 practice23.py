# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 9 , Number 2

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(people):
    # 여기에 코드를 작성해주세요.

    answer = [0 for i in range(4)]

    for j in range(5):
        if people[j] < 95:
            answer[0] += 1
        elif people[j] >= 95 and people[j] < 100:
            answer[1] += 1
        elif people[j] >= 100 and people[j] < 105:
            answer[2] += 1
        elif people[j] >= 105:
            answer[3] += 1

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107]
ret = solution(people)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
