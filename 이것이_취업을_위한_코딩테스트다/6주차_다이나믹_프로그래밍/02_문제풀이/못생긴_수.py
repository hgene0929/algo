'''
[소인수분해 코드]
-  소인수분해 : 
    - 2~n 로 나누어 떨어지거나 그렇지 않거나 둘 중 하나의 케이스로 나뉜다
    - 따라서 코드로 작성할 때에는 나누어떨어지는 경우에는 나누고, 그렇지 않으면 나누는 수를 1 증가시킨다
    - 나누어 떨어질 때마다 나누어지는 수가 소인수가 될 것이다

=> 개선필요 : dp가 아니라 사실 그냥 소인수분해를 구해서 일일이 대조해보았다
'''
def factorization(num):
    if num == 1:
        return [1]
    
    results = []
    idx = 2

    while  idx <= num:
        if num % idx == 0:
            num //= idx
            results.append(idx)
        else:
            idx += 1
    return results

#입력
n = int(input())

#풀이 : n만큼의 dp테이블을 생성하여 1~ 숫자를 살펴보며 해당 숫자가 못생긴 수라면 dp테이블에 삽입
dp = [0] * (n+1)

num = 1
idx = 1
while idx <= n:
    is_prime = True
    results = factorization(num)
    for result in results:
        if result not in (1,2,3,5):
            is_prime = False
            break
    if is_prime:
        dp[idx] = num
        idx += 1
    num += 1

#출력
print(dp[n])