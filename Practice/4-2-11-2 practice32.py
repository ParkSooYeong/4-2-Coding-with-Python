# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Week 11 , Number 2

def solution(sentence):

    str = ''

    for c in sentence:

        # if c != '.' or c != ' ':
        if c != '.' and c != ' ':

            str += c

    size = len(str)

    for i in range(size // 2):

        if str[i] != str[size - 1 - i]:

            return False

    return True

#sentence1 = "never odd or even."
sentence1 = "never odd or veven."
ret1 = solution(sentence1)

print("", ret1)
