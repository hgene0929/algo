import sys

input = sys.stdin.readline

#입력
n = int(input())
students = []
for _ in range(n):
    name,score = map(str,input().split())
    students.append((int(score),name))

#풀이
students.sort()

#출력
for student in students:
    print(student[1], end=' ')