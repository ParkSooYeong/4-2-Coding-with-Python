# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 7 , Number 1

def fpython0():
    print("Python")
    print("파이썬")

def fpython1():
    print("Python")
print("파이썬")

fpython0()
print("\n")
fpython1()

print("\n")

def fadd0(n, m):
    s = n + m
    print(n, "+", m, "=", s)

a = 3
b = 4
fadd0(a, b)

print("\n")

def fadd1(n, m):
    s = n + m
    print(n, "+", m, "=", s)
    return(s)

a = 3
b = 4
c = fadd1(a, b)
print(c)

print("\n")

def avg(a, b):
    s = (a + b) / 2
    return s

in1 = int(input("값1 : "))
in2 = int(input("값2 : "))
r = avg(in1, in2)
print("평균 =", r)
