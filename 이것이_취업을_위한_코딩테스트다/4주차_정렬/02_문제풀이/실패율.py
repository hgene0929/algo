import heapq

def solution(N, stages):
    stages.sort()
    
    remains = [0] * (N+2)
    for stage in stages:
        remains[stage] += 1
    remains = remains[1:-1]
    
    q = []
    cleared = len(stages)
    for idx,remain in enumerate(remains):
        if cleared == 0:
            heapq.heappush(q, (0, idx+1))
        else:
            heapq.heappush(q, (-(remain/cleared),idx+1))
        cleared -= remain
    
    results = []
    while q:
        results.append(heapq.heappop(q)[1])
    
    return results