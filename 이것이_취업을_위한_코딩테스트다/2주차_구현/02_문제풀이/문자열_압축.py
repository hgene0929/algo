'''
[문자열 압축]
- 비손실 압축 방법: 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현.
- 구해야하는 것: 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법 -> 몇개 단위로 압축해야하는가?
- 아이디어:
    - 일단 압축하려면? 최소 1번은 중복되어야 한다? => 그러니까 압축할 수 있는 단위의 최대 자릿수는 전체 자릿수 // 2!
    - 그러면,, 가능한 자릿수는 "1 ~ 주어진 s의 자릿수//2" => 모두 각각 살펴보면서 가장 짧은지 확인 
    - s 의 최대길이는 1,000 -> 1 ~ 500 최악의 경우 괜찮을듯,, 어차피 이진탐색은 특정 타깃이 있는게 아니고,, 비교 불가,, ㅇㅋ
'''
from collections import deque

#풀이
def solution(s):
    length = len(s)
    result = length #압축해야하는 경우 -> 주어진 s의 길이보다 짧은 경우만

    for unit in range(1,length//2+1): #가능한 단위를 모두 살펴보며
        sq = deque(s)
        num,prev,temp = 1,'',''

        while sq:
            if len(sq) <= unit: #남은 문자열이 단위보다 작거나 같으면, 종료
                break

            now = ''
            for _ in range(unit): #단위만큼 문자열 쪼개기
                now += sq.popleft()
            
            if prev == '': #새롭게 시작하는 거면, 우선 비교대상에 현재 쪼갠 문자열 저장
                prev = now
            else:
                if prev == now: #이전 문자열이랑 현재랑 똑같으면 -> 압축가능
                    num += 1
                else: #이전 문자열이랑 다르면 -> 압축불가
                    if num == 1:
                        temp += prev
                    else:
                        temp += str(num)+prev
                        num = 1
                    prev = now
        
        #남아있는 문자열 처리
        remain = ''
        while sq:
            remain += sq.popleft()
        if prev == remain:
            temp += str(num+1)+prev
        else:
            if num == 1:
                temp += prev+remain
            else:
                temp += str(num)+prev+remain

        #더 작은 길이로 압축할 수 있다면 최소길이 갱신
        result = min(result, len(temp))
    
    return result
            
#테스트케이스
s = 'xababcdcdababcdcd'
print(solution(s))