'''
[숫자 카드 게임]
- 구해야 하는 것 : 주어진 숫자 중 최종적으로 가장 큰 숫자 뽑기
- 규칙 : 
    1. 숫자 카드는 N*M 2차원 배열 형태로 주어진다
    2. 먼저 뽑고자하는 카드가 포함된 행을 선택한다
    3. 선택한 행 중 가장 작은 숫자를 뽑는다
- 아이디어 : 각 행에서 가장 작은 숫자를 뽑아낸 다음, 그 중 가장 큰 수를 뽑는 것은 어떤가
'''
#입력 
n,m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

#풀이
result = 0
for num in nums:
    min_num = min(num)
    result = max(result, min_num)

#출력
print(result)