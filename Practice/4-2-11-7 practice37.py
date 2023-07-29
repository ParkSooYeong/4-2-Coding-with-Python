# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Week 11 , Number 6

def solution(attack, recovery, hp):

    count = 0

    for i in range(hp):

        if i % 2 == 1:

            hp -= attack
            count += 1

        if i % 2 == 0:

            hp += recovery

        if hp <= 0:

            break

    return count


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
attack = 30
recovery = 10
hp = 60
ret = solution(attack, recovery, hp)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
