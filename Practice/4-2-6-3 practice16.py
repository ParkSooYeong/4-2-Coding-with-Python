# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 6 , Number 3

size = [0 for i in range(5)]
count = [0 for i in range(5)]

for i in range(0, 5, 1):
    
    size[i] = int(input("치수를 입력하세요. : "))

    if(size[i] > 100):
        count[0] += 1
        print("XL")
    elif((size[i] <= 100) and (size[i] > 95)):
        count[1] += 1
        print("L")
    elif((size[i] <= 95) and (size[i] > 90)):
        count[2] += 1
        print("M")
    elif((size[i] <= 90) and (size[i] > 85)):
        count[3] += 1
        print("S")
    elif((size[i] <= 85) and (size[i] > 0)):
        count[4] += 1
        print("XS")

print("\n")
print(size)
print("\n")
print(count)
