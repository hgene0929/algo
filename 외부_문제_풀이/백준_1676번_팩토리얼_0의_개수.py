'''
[팩토리얼 0의 개수]
- 구해야하는 것 : N! 의 뒤에서부터 연속되는 0의 개수
- 아이디어 : 
    1. math.factorial 의 값을 str형으로 변환한 후, 뒤에서부터 0이 아닌 수가 나올 때까지 0을 세는 방법 => 효율성 점수를 못받음.
    2. 1번보다 효율적인 코드가 필요함..!
        - 원리 : n! 의 뒤에서부터 연속되는 숫자는 n이 5의 제곱수로 나누어 떨어지는 횟수이다.
        - 즉, N >= 5 -> N//5가 답, N >= 25 -> N//5 + N//25가 답, N >= 125 -> N//5 + N//25 + N//125가 답 이다.
'''
#입력
n = int(input())

#풀이 : N은 최대 500으로 5^4인 625는 입력되지 않을 것 => N//5,25,125의 합이 정답
cnt = 0
while n != 0: #N이 더이상 5로 나누어지지 않을 때까지 반복
    n //= 5
    cnt += n

#출력
print(cnt)