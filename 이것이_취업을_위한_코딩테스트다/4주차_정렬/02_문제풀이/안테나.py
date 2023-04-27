'''
구해야하는 것: 일직선 좌표 위의 집들 중 다른 집들의 좌표와의 거리가 최소로 만들어주는 집의 위치.
아이디어: 가장 중간에 있으면 다른 집들과의 거리가 최소일 것이다 -> 중간은? 리스트의 가운데 인덱스 -> 가운데 인덱스가 2개라면?(리스트의 길이가 짝수인 경우) -> 최소값 => 짝수 = n//2-1, 홀수 = n//2
'''
import sys

input = sys.stdin.readline

#풀이
def solution(n, houses):
    result = 0
    houses.sort()
    if n % 2 == 0:
        result = houses[n//2-1]
    else:
        result = houses[n//2]
    return result

#테스트케이스
n = int(input())
houses = list(map(int, input().split()))

print(solution(n,houses))