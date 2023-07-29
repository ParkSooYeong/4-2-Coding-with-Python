# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Week 11 , Number 6

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(words):

    answer = ""

    for w in words:

        if len(w) >= 5:

            answer += w

    if len(answer) < 1:

        answer = "empty"

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("", ret1)
