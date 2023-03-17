'''
[문자열 뒤집기]
- 주어진 문자열 S는 0,1로 구성됨.
- 0,1 중 하나를 골라서 뒤집어서 전체를 똑같이 만들어야 함.
- 이때, 연속된 문자를 뒤집는 건 -> 카운트 1로 간주.
- 구해야하는 것: 문자열 S를 뒤집어 똑같이 만드는 최소횟수.
- 아이디어:
    - 경우의 수:
        - 1 <-> 0 으로 변경횟수가 홀수라면? 어떤것을 변경하는 상관없이 최소횟수 보장.
        - 1 <-> 0 으로 변경횟수가 짝수라면? 처음 시작하는 문자와 반대되는 문자를 변경하는 것이 최소횟수 보장.
    => 그러면, 그냥 문자열 S가 시작하는 문자와 반대되는 문자를 변경하면 무조건 최소횟수 보장 아닌가?!
'''
#입력
s = list(map(int, input()))

#풀이
target = 0
if s[0] == 0:
    target = 1

cnt = 0
for i in range(1,len(s)):
    if s[i] == target and s[i-1] != target:
        cnt += 1

#출력
print(cnt)