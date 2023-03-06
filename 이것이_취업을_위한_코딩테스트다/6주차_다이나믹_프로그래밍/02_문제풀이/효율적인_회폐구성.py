'''
[큰 단위의 화폐는 작은 단위 화폐의 배수임을 보장할 수 X]
- 위의 조건 때문에 그리디(매번 가장 큰 화폐로 가능한 최대한 많이 나누기)로는 해결 X
- 작은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐개수를 찾아야 한다
- 점화식 : 
    - 가능한 경우 : a[i] = min(a[i], a[i-k]+1)
    - 불가능한 경우 : a[i] = 최대수+1
- EX. 현재 화폐 단위가 2와 3이 있다고 가정하면, 
    m을 만드는 최소 개수는 m-2를 만드는 최소 개수와 m-3을 만드는 최소 개수 중 더 작은 값+1이다
'''
import sys
input = sys.stdin.readline

#입력
n,m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input().rstrip()))

#풀이
dp = [10001] * (m+1) #0~m까지 각 숫자를 구성하는 최소 화폐 개수 저장용 dp테이블
dp[0] = 0 #0원을 구성하는 화폐의 최소개수는 0개

for i in range(n): #(1)가지고 있는 화폐단위 살펴보면서
    for j in range(money[i], m+1): #(2)그 화폐단위보다 큰 금액을 구성할 수 있는지 살펴본다(이때, 가지고 있는 화폐단위보다 작은 금액은 구성불가능하다)
        if dp[j - money[i]] != 10001: #(3)구성가능하다면 점화식 적용
            dp[j] = min(dp[j], dp[j-money[i]]+1)

#출력
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])