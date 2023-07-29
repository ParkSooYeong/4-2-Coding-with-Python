# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 10 , Number 7

def solution(scores):

    count = 0

    for s in range(len(scores) - 1): # len(scores) - 1

        if scores[s] <= 200:

            count += 1

    return count

scores = [100, 200, 300, 400]
ret = solution(scores)
print(ret)
