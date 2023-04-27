import sys

input = sys.stdin.readline

#풀이
def solution(array,target,start,end):
    result = 0
    while start <= end:
        mid = (start+end)//2
        #로직시작
        temp = 0
        for el in array:
            if el > mid:
                temp += el-mid
        #로직끝
        if temp < target:
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result

#테스트케이스
n,m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
print(solution(array,m,0,array[-1]))