#입력
s1 = input()
s2 = input()

#풀이
l1 = len(s1)
l2 = len(s2)

dp = [[0]*(l2+1) for _ in range(l1+1)]
for i in range(1,l1+1):
    dp[i][0] = i
for i in range(1,l2+1):
    dp[0][i] = i

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

#출력
print(dp[l1][l2])