'''
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수.
주어진 것: 전체 스테이지 개수 N, 사용자가 현재 멈춰있는 스테이지의 번호 배열 stages.
구해야하는 것: 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return.
'''
import heapq

#풀이1
def solution(N, stages):
    results = [] 
    cnt_players = len(stages) #스테이지에 도달한 플레이어 수

    for i in range(1,N+1): #각 스테이지 단계
        if cnt_players == 0:
            results.append((0,i)) #스테이지에 도달한 사람이 없는 경우 -> 0으로 나누면 런타임 에러 나오니까 잘 처리
            continue
        cnt = stages.count(i) #스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        results.append((cnt/cnt_players,i))
        cnt_players -= cnt #스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수만큼 다음 스테이지부턴 도달하지 못할 것이므로 갱신

    results.sort(key=lambda x:[-x[0],x[1]])
    answer = [x[1] for x in results]
    return answer

#풀이2
def solution(N, stages):
    stages.sort()
    
    remains = [0] * (N+2) #현재 단계에 남아있는 사람 수
    for stage in stages:
        remains[stage] += 1
    
    q = []
    cleared = len(stages) #현재 단계에 도달한 사람 수
    for idx,remain in enumerate(remains[1:-1]):
        if cleared == 0: #스테이지에 도달한 사람이 한명도 없다면 -> 실패율 == 0
            heapq.heappush(q, (0, idx+1))
        else:
            heapq.heappush(q, (-(remain/cleared),idx+1)) #실패율 = 현재 단계에 남아있는 사람 수 / 현재 단계에 도달한 사람 수
        cleared -= remain #현재 단계에 남아있는 사람은 다음 단게에 도달하지 X
    
    results = []
    while q:
        results.append(heapq.heappop(q)[1])
    
    return results

#풀이3
def solution(N, stages):
    results = []
    arrived = len(stages)

    for level in range(1,N+1):
        fail = 0
        not_cleared = stages.count(level)
        if arrived == 0:
            fail = 0
        else:
            fail = not_cleared/arrived
        results.append((fail,level))
        arrived -= not_cleared

    results.sort(key=lambda x:x[0],reverse=True)
    answer = []
    for result in results:
        answer.append(result[1])
    return answer