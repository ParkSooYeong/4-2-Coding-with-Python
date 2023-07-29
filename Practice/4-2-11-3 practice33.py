# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Week 11 , Number 3

def solution(characters):

    result = ""
    result += characters[0]

    # for i in range(len(characters)):
    for i in range(1, len(characters)):

        if characters[i - 1] != characters[i]:

            result += characters[i]

    return result

characters = "senteeeencccccceeee"
ret = solution(characters)

print("", ret, ".")
