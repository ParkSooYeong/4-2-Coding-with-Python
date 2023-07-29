# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Week 11 , Number 1

def solution(scores):

    count = 0

    # for s in scores:
    for s in range(len(scores)):

        # if 650 <= or s < 800:
        # if 650 <= s and s < 800: , if 650 <= s < 800: (<- 모범답안은 아님)
        if 650 <= scores[s] < 800:

            count += 1 # count = count + 1

    return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

print("Solution : return value of the function is", ret, ".")


# 리스트 자체를 이용하는 방법
# for s in scores:
#   if 650 <= s < 800:
#       count += 1
#       print(count)

# 리스트의 크기를 이용하는 방법
# for i in range(len(scores)):
#   if 650 <= scores[i] < 800:
#       count += 1
#       print(count)

# 또 다른 예시
# gloves = [1, 2, 2, 4, 4, 7]
# counter = [0 for _ in range(len(gloves) + 2)] (<- 0과 마지막 수 7을 포함하기 위해 +2를 함)
# for x in gloves:
#   counter[x] += 1
#   print(counter)

#[0, 0, 0, 0, 0, 0, 0, 0]
#[0, 1, 0, 0, 0, 0, 0, 0]
#[0, 1, 1, 0, 0, 0, 0, 0]
#[0, 1, 2, 0, 0, 0, 0, 0]
#[0, 1, 2, 0, 1, 0, 0, 0]
#[0, 1, 2, 0, 2, 0, 0, 0]
#[0, 1, 2, 0, 2, 0, 0, 1]
