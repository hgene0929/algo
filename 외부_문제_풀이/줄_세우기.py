'''
구해야하는 것: N명의 학생들을 키 순서대로 줄을 세운다
아이디어:
    - 모두의 키 X, 일부 학생들 2명을 비교한 결과만 존재 -> 선수관계 존재하는 정렬 => 위상정렬
'''
import sys
from collections import deque

input = sys.stdin.readline

#풀이
def solution(n,orders,indegree):
    result = []
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now) #진입차수가 0 -> 자기가 지금 우선순위 1순위 => 줄세운다
        for next in orders[now]: #자기보다 우선순위가 높은 친구가 이미 줄을 섰다 -> 이제 우선순위가 증가한다 => 진입차수 -= 1
            indegree[next] -= 1
            if indegree[next] == 0: #우선순위가 증가했을때 1순위라면 => 다음번 줄 설 차례
                q.append(next)
    return result

#테스트케이스
n,m = map(int, input().split())
orders = [[] for _ in range(n+1)]
indegree = [0] * (n+1) #선수관계를 비교하기 위해 각 노드의 진입차수 저장
for _ in range(m):
    a,b = map(int, input().split())
    orders[a].append(b)
    indegree[b] += 1 #b학생 앞에 위치해야하는 노드가 증가 => b의 진입차수 += 1

results = solution(n,orders,indegree)
for result in results:
    print(result, end=' ')