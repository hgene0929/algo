'''
아이디어: 
    - 배열 A원소가 최대가 되려면, K번 연산동안 A의 가장 작은 수 <-> B의 가장 큰 수 하면 됨.
    - 매번 삽입 후 정렬이 되어야 하니까, heapq 사용.
추가: 근데 테스트케이스 보면 10,000,000가 데이터 개수 -> 매번 정렬할 필요도 X => heapq 제거 해봄.
'''
import heapq,sys

input = sys.stdin.readline

#풀이 - heapq 사용
def solution(n,k,a,b):
    aq,bq = [],[]
    for i in range(n):
        heapq.heappush(aq,a[i])
        heapq.heappush(bq,-b[i])
    #원소교체 시작
    for _ in range(k):
        ae = heapq.heappop(aq)
        be = heapq.heappop(bq)
        heapq.heappush(aq,-be)
        heapq.heappush(bq,ae)
    #원소교체 끝
    result = 0
    while aq:
        result += heapq.heappop(aq)
    return result

#풀이 - heapq 사용 X
def solution(k,a,b):
    a.sort()
    b.sort(reverse=True)
    #원소교체시작
    for i in range(k):
        a[i],b[i] = b[i],a[i]
    #원소교체끝
    return sum(a)

#테스트케이스
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(solution(n,k,a,b))