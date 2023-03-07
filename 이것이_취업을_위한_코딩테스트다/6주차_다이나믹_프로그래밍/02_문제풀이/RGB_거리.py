import sys
input = sys.stdin.readline

#입력
n = int(input())
RGB = [list(map(int, input().rstrip().split())) for _ in range(n)]

#풀이 : 서로 인접한 집은 색이 무조건 달라야 한다 -> 각각 R,G,B 와 이전 집의 겹치지 않는 비용을 비교하여 최소값을 구해야 한다
for i in range(1,n):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

#출력
result = min(RGB[n-1])
print(result)