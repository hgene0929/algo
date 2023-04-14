import heapq

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