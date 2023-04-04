'''
[연산자 끼워 넣기]
- 구해야하는 것: 숫자N개 + 연산자N-1개 => 숫자와 숫자 사이에 연산자 하나씩 넣어서 최댓값과 최솟값 출력
- 조건:
    - 숫자 순서 변경 X
    - 연산자 우선순위 X
    - 음수 / 양수 == abs(음수) // 양수
- 아이디어:
    - 결국, 해야하는 것: 연산자 순서만 바꿔가면서 숫자 사이에 넣어서 값 도출 -> 서로 비교 -> min/max 출력
'''
from itertools import permutations
from collections import deque

#풀이
def solution(nums,ops):
    #연산자로 만들 수 있는 모든 경우의 수 계산
    cases = list(permutations(ops,len(ops)))

    result = []
    
    #각 경우의 수 별로 연산 수행
    for case in cases:
        numbers = deque(nums)
        temp = numbers.popleft()
        for op in case:
            number = numbers.popleft()
            if op == '+':
                temp += number
            elif op == '-':
                temp -= number
            elif op == '*':
                temp *= number
            else:
                if temp < 0:
                    t = abs(temp) // number
                    temp = -t
                else:
                    temp //= number
        result.append(temp)
    
    return min(result),max(result)

#테스트케이스
n = int(input())
nums = list(map(int, input().split()))
cnt_plus,cnt_minus,cnt_multiply,cnt_divide = map(int, input().split())

ops = []
for _ in range(cnt_plus):
    ops.append('+')
for _ in range(cnt_minus):
    ops.append('-')
for _ in range(cnt_multiply):
    ops.append('*')
for _ in range(cnt_divide):
    ops.append('/')

min_num,max_num = solution(nums,ops)
print(f'{max_num}\n{min_num}')