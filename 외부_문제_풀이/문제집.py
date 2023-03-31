'''
[문제집]
- 구해야하는 것: 난이도 순서대로 출제된 문제의 선수관계를 고려하여 문제를 풀 순서 출력 => 위상 정렬
- 조건: 
    1. 먼저 푸는 것이 좋은 문제 -> 문제 간의 선수관계 존재 => 위상정렬
    2. 같은 선수관계라면 쉬운 문제부터 => 오름차순 정렬
'''
import sys,heapq

input = sys.stdin.readline

#풀이
def solution(n,graph,indegree):
    result = []
    q = []

    for i in range(1,n+1):
        if indegree[i] == 0:
            heapq.heappush(q,i) #진입차수가 0이면 이친구가 우선순위 넘버원 + 같은 우선순위에 있으면 난이도 순으로
    
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for next in graph[now]:
            indegree[next] -= 1 #앞의 문제를 하나 해결했으니까, 그 뒤의 문제들 진입차수 -= 1
            if indegree[next] == 0:
                heapq.heappush(q,next)

    return result

#테스트케이스
n,m = map(int, input().split())
indegree = [0] * (n+1) #각 문제별 진입차수 저장
graph = [[] for _ in range(n+1)] #각 문제별 다음으로 풀 수 있는 문제
for _ in range(m):
    a,b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
        indegree[b] += 1

results = solution(n,graph,indegree)
for result in results:
    print(result, end=' ')