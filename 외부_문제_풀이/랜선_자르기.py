'''
구해야하는 것: N개 이상의 랜선으로 나누기 위한(자른다) 최대 랜선 길이
아이디어:
    - 랜선의 최대 길이를 찾아야 한다 -> 탐색이다
    - 그런데 K, N의 입력값이 너무 크다 -> 순차 탐색 불가 -> 이진 탐색 사용
'''
import sys

input = sys.stdin.readline

#풀이
def solution(lines,target,start,end):
    result = 0
    while start <= end:
        mid = (start+end)//2
        total = 0
        for line in lines:
            total += line//mid
        if total < target:
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result

#테스트케이스
k,n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

print(solution(lines,n,1,max(lines))) #주의: 나누기를 해야하는 상황이라면 zeroDivisionError를 피하기 위해 0이 아니라, 1부터 시작해야한다