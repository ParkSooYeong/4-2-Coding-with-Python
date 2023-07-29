# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 5 , Number 8

XS = 0
S = 0
M = 0
L = 0
XL = 0

for i in range(0,10,1):

    size = int(input("학생의 치수를 입력하세요. : "))

    if 85 >= size >= 0:
        XS += 1
    elif 90 >= size >= 86:
        S += 1
    elif 95 >= size >= 91:
        M += 1
    elif 100 >= size >= 96:
        L += 1
    else:
        XL += 1

print("\nXS 사이즈는", XS, "명 입니다.\n")
print("S 사이즈는", S, "명 입니다.\n")
print("M 사이즈는", M, "명 입니다.\n")
print("L 사이즈는", L, "명 입니다.\n")
print("XL 사이즈는", XL, "명 입니다.\n")
