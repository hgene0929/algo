'''
구해야하는 것: M명이 심사를 받는데 걸리는 총시간의 최솟값
입국심사 원리:
    - 입국심사대 N개, k번 심사대에서 심사를 하는데 소요시간은 T[k]
    - 한 심사대에 한번에 한사람만 심사 가능
    - 줄을 서있다가 빈 심사대가 나오면 이동가능 -> 근데 이동해서 시간이 단축될 때만 이동가능 -> 여기서 기다리는시간 > 이동해서 받는 심사대에서의 심사시간 일때만 이동가능
'''
import sys

input = sys.stdin.readline

#풀이
def solution(target,times,start,end):
    result = 0
    while start <= end:
        #임시 결과값 갱신 => 이진탐색
        mid = (start+end)//2
        #핵심로직 => 임시 최소시간동안 각 심사대별로 심사받을 수 있는 인원수 = 임시최소시간(mid) // 각 심사대의 심사시간(time)
        cnt = 0 #심사받은 인원수
        for time in times:
            cnt += mid//time
        #탐색범위갱신 => 심사받은 인원수가 m명보다 작으면 -> 최소심사시간을 늘려야함, 심사받은 인원수가 m명보다 같거나 크면 -> 최소심사시간을 줄일 수 있을때까지 줄임
        if cnt < target:
            start = mid+1
        else:
            result = mid
            end = mid-1
    return result

#테스트케이스
n,m = map(int, input().split())
times = [int(input()) for _ in range(n)]
times.sort()

print(solution(m,times,1,times[n-1]*m)) #탐색범위: min = 1명(m=1)일때 -> 심사시간의 최솟값, max = 최대시간(max(times))으로 m명이 모두 심사를 받는 경우