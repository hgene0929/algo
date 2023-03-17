'''
[볼링공 고르기]
- 구해야하는 것: 주어진 볼링공 N개의 조합(2), 이때 조합에 포함된 볼링공 2개의 무게는 서로 달라야 한다.
- 아이디어:
    - itertools.combinations()로 조합을 모두 구한 다음, 속한 원소의 무게가 서로 다른 것을 제외할 것인가..
    - 조합을 직접 구현하면서 서로 무게가 같으면 제외할 것인가?
    - 어떤 걸로 해도 상관없을듯??
- 효율적인 방법:
    - 그런데 위와 같은 방식으로 조합을 구현할 경우, 현재는 괜찮지만,, 만약 공의 개수가 1000가 아니라, 100,000개를 넘어가면 -> 비효율적인 코드가 될 것..
    - 생각해볼만한 방법 아이디어:
        - N개의 원소들을 2개씩 조합하는 공식: N * (N-1).
        - 제외해야할 상황: a == b가 되는 상황.
        - a,b가 될 수 있는 값의 범위: 1 ~ 10 => 기준을 두어 a가 무게 1~10개인 공을 확실히 잡는다고 가정했을때 b가 고를 수 있는 경우의 수의 총합 이 정답?!
        => a : 1 -> b : N - (무게가 1인 공의 개수), a : 2 -> b : N - (무게가 2인 공의 개수), ... , a : 10 -> b : N - (무게가 10인 공의 개수) 의 총합.
'''
from itertools import combinations

#(풀이 1)itertools.combinations() 활용하는 방법
def itertools_combinations(a):
    datas = list(combinations(a,2)) #조합 구함(무게가 서로 같은 공 고른 경우도 포함되어 있음) => 최대 1000*999
    cnt = 0
    for a,b in datas:
        if a != b: #이때, 무게가 서로 같은 공을 고른 경우를 제외시켜버림ㄴ
            cnt += 1
    return cnt

#(풀이 2)직접 조합을 구하는 과정을 구현하여 조합을 구하면서 무게가 같은 공을 고르는 경우를 제외시키는 방법 => 최대 1000*999
def cutom_combinations(n,a):
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] != a[j]:
                cnt += 1
    return cnt

#(풀이 3)가장 효율적인 방법: a가 고른 공의 무게가 정해져있다고 가정하고 -> 그 무게와 겹치지 않는 공의 개수의 합을 10번 반복하며 구한다 => 최대 10*9
def best_combinations(n,m,a):
    weights = [0] * (m+1)
    for i in range(n):
        weights[a[i]] += 1 #공 무게마다 몇개가 있는지 저장(계수정렬)

    cnt = 0
    for i in range(1,m+1): #a가 든 공의 무게를 제외한 공의 개수가 각 무게마다 나올 수 있는 경우의 수
        n -= weights[i] #조합이니까 누적뺄셈
        cnt += weights[i] * n #a의 경우의 수 * b의 경우의 수
    
    return cnt



#테스트케이스
n,m = map(int, input().split())
balls = list(map(int, input().split()))

print(itertools_combinations(balls))
print(cutom_combinations(n,balls))
print(best_combinations(n,m,balls))