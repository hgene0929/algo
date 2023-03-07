#입력
n = int(input())
nums = list(map(int, input().split()))

#풀이 : LIS -> 1에서부터 시작(dp) -> 증가하는 수인 경우(조건만족) 이전의 수에서 누적+1
dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

#출력
result = max(dp)
print(result)