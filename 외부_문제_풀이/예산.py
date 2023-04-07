'''
구해야하는 것: 가능한 한 최대의 총 예산
예상 배정 규칙:
    - 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
    - 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 요청에는 모두 상한액 배정
아이디어: 
    - 모든 요청 배정될 수 있는지 확인 
        - 배정가능: 그냥 모두 배정
        - 배정불가: 각 요청을 확인하면서 상한액을 구해야함 -> 입력값 굉장히 큼 => 이진탐색 GO(파라메트릭 서치)
'''
import sys

input = sys.stdin.readline

#풀이
def binary_search(requests,target,start,end):
    result = 0
    while start <= end:
        mid = (start+end)//2
        #파라메트릭 서치 핵심로직: 상한액보다 큰 요청금액은 상한액만큼만 주고, 나머지는 요청금액 그대로를 준다
        total = 0
        for request in requests:
            if request > mid:
                total += mid
            else:
                total += request
        #범위갱신: 해당 상한액으로 구한 총 금액이 주어진 m보다 크면 상한액 줄여야 함, 작거나 같으면 일단 가능 최대한 더 늘려본다
        if total > target:
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result


def solution(n,m,requests):
    #모든 요청 배정될 수 있는지 확인
    if sum(requests) <= m: #배정가능 -> 그냥 모두 배정
        return max(requests)
    #배정불가 -> 상한액 구하는 이진탐색
    return binary_search(requests,m,0,max(requests)) #탐색범위: 0 ~ 가장 큰 예산 요청금액

#테스트케이스
n = int(input())
requests = list(map(int, input().split()))
m = int(input())

print(solution(n,m,requests))