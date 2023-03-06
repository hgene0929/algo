#입력
n = int(input())
food = list(map(int, input().split()))

#풀이
dp = [0] * n
dp[0] = food[0]
dp[1] = max(food[0], food[1])

for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2]+food[i])

#출력
print(dp[n-1])