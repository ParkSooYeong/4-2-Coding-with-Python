# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 5 , Number 3

import sys

print("상점에 오신걸 환영합니다. 원하시는 아이템을 선택해주세요.\n")
print("1. 무한의 대검")
print("2. 라바돈의 죽음모자")
print("3. 워모그의 갑옷")
print("4. 미카엘의 축복")
print("5. 투명 감지 와드\n")
print("이외 숫자를 입력하시면 프로그램이 종료됩니다.\n")

for i in range(0, 5, 1):

    select = int(input("메뉴 숫자 입력 : "))

    if select == 1:
        print(select, "번 아이템인 '무한의 대검' 아이템 구매가 완료되었습니다!\n")

    elif select == 2:
        print(select, "번 아이템인 '라바돈의 죽음모자' 아이템 구매가 완료되었습니다!\n")

    elif select == 3:
        print(select, "번 아이템인 '워모그의 갑옷' 아이템 구매가 완료되었습니다!\n")

    elif select == 4:
        print(select, "번 아이템인 '미카엘의 축복' 아이템 구매가 완료되었습니다!\n")

    elif select == 5:
        print(select, "번 아이템인 '투명 감지 와드' 아이템 구매가 완료되었습니다!\n")

    else:
        print("행운을 빕니다.\n")
        sys.exit()
