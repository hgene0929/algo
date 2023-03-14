## 그래프 이론
-------------------

#### 서로소 집합 알고리즘
-------------------
- 서로소 집합이란 <em>공통 원소가 없는 두 집합</em>을 의미한다.
- 서로소 집합 자료구조 
    - <em>서로소 부분 집합들로 나누어진 원소들의 데이터를 처리</em>하기 위한 자료구조이다.
    - 서로소 집합 자료구조는 두 종류의 연산을 지원한다 :
        > 합집합 : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산.
        > 찾기 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산.
    - 동작과정 :
        1. 가장 처음 각 노드들은 자기 자신을 부모로 가집.
        1. Union(A,B)(A < B) => A와 B의 부모노드는 모두 A의 부모노드.
        1. Find(A) => A의 루트노드를 찾아가 해당 루트노드와 같은 루트노드를 가진 모든 노드는 서로 같은 집합에 포함되있음.
    - 서로소 집합 자료구조에서는 <em>연결성</em>을 통해 손쉽게 집합의 형태를 확인할 수 있다.
    - 다만, 기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없고, 부모 테이블을 계속해서 확인하며 거슬러 올라가야 한다.
        - 이에 기본적인 서로소 집합 자료구조는 최악의 경우(합집합 연산이 편향되게 이루어지는 경우) 시간 복잡도 O(V)를 가지는 문제점이 있다. 
        - 따라서 이러한 찾기함수를 최적화하기 위한 방법으로 경로 압축을 이용할 수 있다.
- 경로 압축
    - 찾기 함수를 재귀적으로 호출한 뒤에 <em>부모 테이블 값을 바로 갱신</em>한다.
    - 따라서 경로 압축 기법을 적용하면 각 노드에 대하여 찾기 함수를 호출한 이후에 해당 노드의 루트 노드가 바로 부모 노드가 된다.

- 서로소 집합 자료구조 기본적인 구현
```python
#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = [b]
```
- 서로소 집합 자료구조 찾기함수 최적화(경로 압축) 구현
```python
#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```
<br>
- 서로소 집합을 활용한 사이클 판별
    > 서로소 집합은 <em>무방향 그래프 내에서의 사이클을 판별</em>할 수 있다.
    - 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.
    - 사이클 판별 알고리즘은 다음과 같다.
        1. 각 간선을 하나씩 확인하며 간선을 구성하는 두 노드의 루트 노드를 판별한다.
            - 루트 노드가 서로 다르다면 두 노드에 대하여 합집합 연산을 수행한다.
            - 로트 노드가 서로 같다면 사이클이 발생한 것이다.
        1. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

- 서로소 집합을 활용한 사이클 판별 구현
```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(Union연산)의 개수 입력받기
v,e = map(int, input().split())
#부모 테이블상에서 부모를 자신으로 초기화
parent = [x for x in range(1,v+1)]

is_cycle = False

for i in range(e):
    a,b = map(int, input().split())
    #사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent,b):
        is_cycle = True
        break
    #사이클이 발생하지 않은 경우 합집합
    else:
        union_parent(parent,a,b)

print(f'is there cycle? {is_cycle}')
```

#### 크루스칼 알고리즘
-------------------
- 신장 트리
    > <em>그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프</em>를 의미한다.
    - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이다.
- 최소 신장 트리
    - 최소한의 비용으로 구성되는 신장 트리를 찾아야 하는 경우
    - EX. 예를 들어 N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결된는 도로를 설치하는 경우.
    - 크루스칼 알고리즘으로 해결할 수 있다.
<br>
- 크루스칼 알고리즘
    > 대표적인 <em>최소 신장 트리 알고리즘</em>이다.
    - 그리디 알고리즘으로 분류된다.
    - 동작과정 :
        1. 간선 데이터를 비용에 따라 오름차순 정렬한다.
        1. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
            - 사이클 O -> 최소 신장 트리에 포함 X.
            - 사이클 X -> 최소 신장 트리에 포함 O.
        1. 모든 간선에 대하여 2번의 과정을 반복한다.
        1. 최소 신장 트리에 포함되어 있는 간선의 비용만 모두 더하면, 그 값이 최종 비용에 해당한다.

- 크루스칼 알고리즘 구현
```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [x for x in range(1,v+1)]

#모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

#모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫번 째 원소를 비용으로 설정
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    #사이클이 발생하지 않는 경우에만 최소신장트리에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
```

#### 위상 정렬 알고리즘
-------------------
- 진입차수 & 진출차수
    - 진입차수 : 특정한 노드로 들어오는 간선의 개수.
    - 진출차수 : 특정한 노드에서 나가는 간선의 개수.
<br>
- 위상 정렬 
    > <em>사이클이 없는 방향 그래프</em>의 모든 노드를 <em>방향성에 거스르지 않도록 순서대로 나열</em>하는 것을 의미한다.
    - EX. 선수과목을 고려한 학습 순서 설정.
    - 동작과정 :
        1. 진입차수가 0인 모든 노드를 큐에 넣는다.
        1. 큐가 빌 때까지 다음의 과정을 반복한다.
            1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
            1. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
        1. 결과적으로 <em>각 노드가 큐에 들어온 순서 == 위상 정렬 결과</em>이다.
    - 특징 :
        - 위상 정렬은 사이클이 없는 방향 그래프에서만 수행할 수 있다.
        - 위상 정렬에는 여러 가지 답이 존재할 수 있다.
            - 한단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면 여러 가지 답이 존재한다.
        - 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
            - 사이클에 포함된 원소 중에서 어떠한 원소도 큐에 들어가지 못한다.
        - 스택을 활용한 DFS를 이용해 위상 정렬을 수행할 수도 있다.

- 위상 정렬 구현
```python
from collections import deque

v,e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

#위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    #처음 시작시 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    #큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for next in graph[now]:
            indegree[next] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[next] == 0:
                q.append(next)

    return result

for res in topology_sort():
    print(res)
```