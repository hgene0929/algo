'''
[가장 긴 증가하는 부분 수열(LIS)]
- 하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제
- 점화식 : 모든 0 <= j < i에 대하여 dp[i] = max(dp[i], dp[j]+1) if array[j] < array[i]
- 부가설명 :
    - dp테이블에 저장되는 값은 각 인덱스가 0번째 원소부터 몇번째 누적된 내림차순(조건을 만족하는) 수인지
    - 따라서 만약 j < i이고, array[j] < array[i]라면 오름차순 조건을 만족하는 것이므로 기존의 증가하던 개수에 누적하여 개수를 늘려간다
    - 해당 문제는 내림차순이므로, LIS알고리즘을 변형하여 사용가능할 것이다
'''
#입력
n = int(input())
power = list(map(int, input().split()))

#풀이
#(1)LIS활용(내림차순->오름차순)
power.reverse()

#(2)dp태이블 생성 및 초기화
dp = [1] * n

#(3)점화식
for i in range(1,n):
    for j in range(i):
        if power[j] < power[i]:
            dp[i] = max(dp[i], dp[j]+1)

#출력
result = n - max(dp)
print(result)