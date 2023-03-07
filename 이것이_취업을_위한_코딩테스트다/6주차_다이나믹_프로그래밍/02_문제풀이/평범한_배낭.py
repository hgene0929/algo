'''
[냅색 문제]
- 선정할 수 있는 원소의 최대 조건이 정해져 있고, 일정 가치를 채워야 할 때 가치의 합이 최대가 되도록 한다
- 점화식 :
    dp[물건번호][물건무게] = max(현재물건가치 + dp[이전물건][현재가방무게-현재물건무게], dp[이전물건][현재가방무게])
'''
import sys
input = sys.stdin.readline

#입력
n,k = map(int, input().split())
stuff = [(0,0)]
for _ in range(n):
    stuff.append(tuple(map(int, input().rstrip().split())))

#풀이
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = stuff[i][0],stuff[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j] #현재물건의 무게가 허용 X -> 가방의 무게 유지
        else:
            dp[i][j] = max(dp[i-1][j], v+dp[i-1][j-w]) #현재물건의 무게 허용 O -> 현재 물건의 무게를 더하는 것 / 가방무게를 유지하는 것 중 더 이득인 값 선택(현재 물건의 가치가 더 커서 바로 이전의 물건을 빼고, 대체하는 것과 동일)

#출력
result = dp[n][k]
print(result)