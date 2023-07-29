# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 4 , Number 13

opnd1 = int(input("피연산자 1 : "))
opnd2 = int(input("피연산자 2 : "))

print(opnd1, "*", opnd2)

print("= (", (opnd1 // 100), "+", (opnd1 // 10 % 10), "+", (opnd1 % 10), ") *", opnd2)
print("= (", (opnd1 // 100), "*", opnd2, ") + (", (opnd1 // 10 % 10), "*", opnd2, ") + (", (opnd1 % 10), "*", opnd2, ")")
print("=", ((opnd1 // 100) * opnd2), "+", ((opnd1 // 10 % 10) * opnd2), "+", ((opnd1 % 10) * opnd2))
print("=", opnd1 * opnd2)
