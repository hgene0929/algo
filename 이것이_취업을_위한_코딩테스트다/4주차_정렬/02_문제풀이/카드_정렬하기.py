'''
아이디어: 매번 묶음의 수가 최소가 되도록 골라야하니까 묶음을 합하고 난 다음에는 매번 정렬을 해주어야 한다 => heapq 사용해볼만 하다.
'''
import sys,heapq

input = sys.stdin.readline

#풀이
def solution(cards):
    result = 0

    q = []
    for card in cards:
        heapq.heappush(q,card)

    while len(q) > 1:
        c1,c2 = heapq.heappop(q),heapq.heappop(q)
        result += c1+c2
        heapq.heappush(q,c1+c2)
    
    return result

#테스트케이스
n = int(input())
cards = [int(input().rstrip()) for _ in range(n)]

print(solution(cards))