'''
[괄호 변환]
- 구해야하는 것: p -> 올바른 문자열
- 괄호변환 규칙:
    - 균형잡힌 괄호 문자열 = ( 개수와 )개수가 똑같음
    - 올바른 괄호 문자열 = (와 )의 짝이 맞는 균형잡힌 괄호 문자열
    - 균형잡힌 괄호 문자열 -> 올바른 괄호 문자열: 
        1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
        2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있음
        3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행
            3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환
        4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행
            4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            4-3. ')'를 다시 붙입니다. 
            4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
            4-5. 생성된 문자열을 반환합니다.
- 아이디어: 
    - 규칙대로 그대로 따라 구현:
        - 1 : return 바로 해버림
        - 2 : u는 더이상 쪼개지지 않는 문자열 + v는 빈문자열 혹은 그냥 남은거 => p 처음부터 확인해서 균형잡힌 문자열이 처음으로 되는 시점에 슬라이스
        => 핵심: 1,2번에 대해 재귀적인 코드 구성할 것
'''
#풀이
def check(p):
    s = []
    for i in range(len(p)):
        if p[i] == '(':
            s.append(p[i])
        else:
            if len(s) == 0 or s[-1] == ')':
                return False
            else:
                s.pop()
    return True

def seperate(p):
    left,right = 0,0
    for i in range(len(p)):
        if p[i] == ')':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i+1],p[i+1:] #u,v
        
def transform(p):
    res = ''
    for i in range(len(p)):
        if p[i] == '(':
            res += ')'
        else:
            res += '('
    return res

def solution(p):
    answer = ''
    if len(p) == 0 or check(p):
        return p
    u,v = seperate(p)
    if check(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        answer += transform(u[1:-1])
    return answer

#테스트케이스
p = "()))((()"
print(solution(p))