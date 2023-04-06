'''
구해야하는 것: c개의 공유기를 설치하기 위한 집의 위치를 구할 때, 가장 인접한 두 공유기 사이의 거리의 최댓값 출력
아이디어:
    - n개의 리스트 중 c개의 값을 뽑아내야 함
    - 이때 가장 인접합 값의 차이가 최대가 되어야 함
    - 즉, 0 ~ houses[n-1] 의 값 중 c 개 선택 -> 값[i] - 값[j]가 최소인 값이 최대가 되도록 구해야 함
    - 0 ~ houses[n-1]개의 숫자 중 c개를 탐색해야 하는 문제인데, 입력값이 매우 큼 -> 이진탐색 O
'''
import sys

input = sys.stdin.readline

#풀이
def solution(n,house,target,start,end):
    result = 0
    while start <= end:
        mid = (start+end)//2 #임의의 gap
        prev = house[0] #직전에 설치한 집의 좌표 -> 항상 시작은 리스트의 양끝(0,-1)에서 시작하는게 가장 큰 gap을 낼 수 있음
        cnt = 1 #공유기를 설치한 집의 개수
        for i in range(1,n):
            if prev+mid <= house[i]: #직전에 설치한 집의 좌표 + 임의의 gap = 다음 공유기를 설치할 수 있는 집의 좌표의 최소값
                prev = house[i]
                cnt += 1     
        if cnt < target: #공유기를 설치한 집의 개수가 target보다 적으면 -> gap을 줄여야 함
            end = mid-1
        else: #공유기를 설치한 집의 개수가 target보다 같거나 많으면 -> gap을 최대한 늘려본다
            start = mid+1
            result = mid
    return result

#테스트케이스
n,c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

print(solution(n,house,c,1,house[-1]-house[0])) #집이 최소 2개는 있으니까, 최소 gap은 1, 최대 gap은 가장 멀리있는 집 - 가장 가까이 있는 집