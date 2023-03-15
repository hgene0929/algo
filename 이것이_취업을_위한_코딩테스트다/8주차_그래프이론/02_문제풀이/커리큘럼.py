import sys, copy
from collections import deque

input = sys.stdin.readline

#입력
n = int(input())

indegree = [0] * (n+1) #각 강의 진입차수(선수과목) 개수
time = [0] * (n+1) #각 강의 비용(소요시간)
graph = [[] for _ in range(n+1)] #각 강의별 선수과목 리스트

for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i) #선수과목들에 이어 올 수 있는 과목들 추가
        indegree[i] += 1 #선수과목이 있는 강의 진입차수 증가

#풀이: 선수과목 -> 위상 정렬 알고리즘 사용
def topology_sort():
    result = copy.deepcopy(time) #각 강의의 시간을 복사해오기 위함
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            #누적된 강의시간보다 더 큰 강의시간을 찾아야 그게 갱신된 강의시간(누적된 시간을 포함해야하기 때문)
            result[next] = max(result[next], result[now]+time[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    return result

#출력
results = topology_sort()
for result in results:
    print(result)