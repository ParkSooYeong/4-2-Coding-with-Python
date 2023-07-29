# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 6 , Number 2

s = 0

for i in [1, 2, 3, 4, 5]:

    s = s + i

print("s :", s)

print("\n")

s = 0

for i in [1, 2, 3, 4, 5]:

    s = s + i

    print("i :", i, ", s :", s)

print("s :", s)

print("\n")

s = 0

for i in range(1, 21):
    if i % 2 == 1:
        continue

    s = s + i

    print("i :", i, "s :", s)

    if s > 30:
        break

print("i :", i, "s :", s)
