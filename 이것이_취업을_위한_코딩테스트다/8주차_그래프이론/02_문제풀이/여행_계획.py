import sys

input = sys.stdin.readline

#풀이: 서로소집합 알고리즘 바탕 함수 구현
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#입력
n,m = map(int, input().split())
parent = [x for x in range(n+1)]

#서로 연결된 여행지들을 연결시켜준다(합집합 수행)
for i in range(1,n+1):
    datas = list(map(int, input().rstrip().split()))
    for idx,data in enumerate(datas):
        if data == 1:
            union_parent(parent,i,idx+1) #서로 연결된 여행지 i와 idx+1을 연결해준다 -> 나중에 부모를 거슬러올라가면 결국 같을 것임

plan = list(map(int, input().split()))


#풀이: 여행계획에 속한 여행지들이 모두 연결되어 있어야 한다 -> 합집합이어야 한다 -> union()을 통해 합쳐준다(연결되어 있다면 같은 집합, 즉 같은 부모를 가질 것) -> 여행 계획에 속한 여행지들의 부모가 모두 같으면 T, 아니면 F
is_Possible = True

for i in range(m-1):
    if find_parent(parent,plan[i]) != find_parent(parent,plan[i+1]):
        is_Possible = False
        break

#출력
if is_Possible:
    print('YES')
else:
    print('NO')