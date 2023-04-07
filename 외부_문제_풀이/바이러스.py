'''
구해야하는 것: 1번 컴퓨터가 바이러스에 걸렸을때, 전염되어 바이러스에 걸리는 컴퓨터 수
바이러스 전염:
    - 네트워크 상에서 연결되어 있는 모든 컴퓨터에 전염
    - 네트워크 연결은 양방향
    - 숙주는 1번 컴퓨터
아이디어: 그래프 상에서 퍼진다 => DFS
'''
import sys

input = sys.stdin.readline

#풀이
def solution(graph,visited,start):
    result = 0
    s = [start]
    visited[start] = True
    while s:
        now = s.pop()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                result += 1
                s.append(next)
    return result

#테스트케이스
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b) #네트워크 연결은 양방향 => a가 살펴봐야하는 컴퓨터와, b가 살펴봐야 하는 컴퓨터 모두에 추가
    graph[b].append(a)
visited = [False] * (n+1)

print(solution(graph,visited,1))