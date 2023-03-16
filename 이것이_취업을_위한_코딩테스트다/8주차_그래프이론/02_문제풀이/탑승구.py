import sys

input = sys.stdin.readline

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
g = int(input()) #탑승구의 수
p = int(input()) #비행기의 수

parent = [x for x in range(g+1)] #탐승구의 부모 노드 저장

#풀이
result = 0

for _ in range(p):
    data = find_parent(parent,int(input()))
    if data == 0:
        break
    union_parent(parent,data,data-1)
    result += 1

#출력
print(result)