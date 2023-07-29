#def solution(arr):
#    left, right = 0, len(arr)-1                        <- 리스트의 맨 처음과 맨 끝
#    while @@@:                                             left = 0 , right = len(arr)-1
#        arr[left], arr[right] = arr[right], arr[left]  <- 교환구문, C나 Java에는 없는 기능임
#        left += 1                                          1, 3 = 3, 1
#        right -= 1                                         4, 2 = 2, 4
#    return arr

def solution(arr):
    left, right = 0, len(arr)-1
    while left < right: # 왼쪽에서의 접근이 오른쪽에서의 접근보다 커지기 전까지 반복
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")
