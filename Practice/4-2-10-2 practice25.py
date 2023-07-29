#def func_a(month, day):
#    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#    total = 0;
#    for i in ( ):
#        total += ( )
#    total += ( )
#    return total - 1

def func_a(month, day):

    month_num = [31, 28, 31, 30 ,31, 30, 31, 31, 30, 31, 30, 31] # 인덱스가 0부터 시작해서 11까지임

    total = 0                                                    # 전체 일 수 변수 초기화가 반드시 필요함

    for i in range(month - 1):                                   # 입력받은 달까지 위의 리스트를 돌게 됨

        total += month_num[i]                                    # 입력받은 달까지의 일 수를 전체 변수에 더함

    total += day                                                 # 남아있는 순수 일 수를 더함

    return total - 1                                             # 1월 1일 시작이므로 하루를 빼야함
        
def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total
        

#The following is code to output testcase.
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
