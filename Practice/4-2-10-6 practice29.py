# SKU CoE ITE - ParkSooYoung
# Grade 4 , Semester 2 , Chapter 10 , Number 6

# 문제 1. 거스름돈을 계산하는 함수 작성하기
# 김 대리는 업무에 필요한 물건들을 구매하기 위해 현금을 받아 문구점에 가는 길입니다.
# 물건들을 구입한 후 남은 잔액은 다시 반납해야 합니다.
# 예를 들어 구매한 물건들의 가격이 [2100, 3200, 2100, 800]이면 총 구매금액은 8200원입니다.
# 지급받은 현금이 10000원이라면 1800원을 반납하면 됩니다.
# 김 대리가 구매한 물품들의 가격이 들어있는 리스트 price와 받은 금액 money가 매개변수로 주어질 때,
# 반납해야 하는 금액을 return 하도록 solution 함수를 완성해주세요.
# 단, 모자라는 경우 -1을 반환하도록 해주세요.

# 코드
def solution(price, money):
    
    answer = 0

    for i in price:

        money -= i

    answer = money

    if answer < 0:

        answer = -1

    return answer

# 다른 풀이
# 

# 실행
price = [2100, 3200, 2100, 800]
money = 10000
ret = solution(price, money)
print(ret)
