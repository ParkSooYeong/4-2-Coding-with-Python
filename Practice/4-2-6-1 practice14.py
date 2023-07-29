# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 6 , Number 1

for i in range(0, 10, 1):
    
    ID = str(input("새 아이디 : "))
    PW = str(input("새 패스워드 : "))

    if (ID == "성결대학교") and (PW == "파이데이아1"):
        print("접속을 환영합니다.")
        break
        
    elif (ID != "성결대학교") or (PW != "파이데이아1"):
        print("아이디와 패스워드를 정확히 입력하세요.")
