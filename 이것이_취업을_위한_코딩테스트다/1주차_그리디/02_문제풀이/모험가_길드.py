'''
[모험가 길드]
- 구해야하는 것 : N명의 모험가를 최대한 많은 그룹으로 분할했을 때, 분할된 그룹의 수.
- 그룹 분할 조건 : 
    - 공포도 X가 속한 그룹의 최소 인원 수는 X이다.
        - 즉, 각 리스트(그룹)의 최대 원소값(공포도)은 그 그룹의 최소 길이(인원수)이다.
    - 꼭 모든 모험가가 그룹에 속할 필요는 없다.
- 아이디어 : 공포도가 작을수록 더 작은 인원으로 그룹을 구성할 수 있지 않을까? => 공포도를 오름차순 정렬하여 그룹을 생성하면 되지 않나??
'''
#입력
n = int(input())
fear = list(map(int, input().split()))

#풀이
fear.sort()

cnt = 0
temp_cnt = 0 #각 그룹의 최소인원 저장

for max_fear in fear: #공포도 리스트는 오름차순 정렬되어있기 때문에 매번 더 크거나 같은 공포도가 max_fear이 될 것임
    temp_cnt += 1 #각 그룹에 인원추가
    if temp_cnt >= max_fear: #각 그룹에 추가된 인원이 현재 최대 공포도보다 크거나 같다면 분할
        temp_cnt = 0
        cnt += 1

#출력
print(cnt)