def func_a(arr):
    counter = [0 for _ in range(1001)] # 숫자별 몇개인지 파악하는 용도의 리스
    for x in arr:
        counter[x] += 1
        #print(counter) # 추가해서 무슨 값이 나오는지 확인용
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
            print(ret)
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

#def solution(arr):
#    counter = func_@@@(@@@)
#    max_cnt = func_@@@(@@@)
#    min_cnt = func_@@@(@@@)
#    return max_cnt // min_cnt

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

#The following is code to output testcase.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
