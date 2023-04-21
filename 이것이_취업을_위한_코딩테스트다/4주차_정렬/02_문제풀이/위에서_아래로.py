import sys

input = sys.stdin.readline

#입력
n = int(input())
numbers = [int(input().rstrip()) for _ in range(n)]
#풀이
numbers.sort(reverse=True)
#출력
for number in numbers:
    print(number, end=' ')