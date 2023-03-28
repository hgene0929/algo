'''
[치킨 배달]
- 구해야하는 것: 도시의 치킨거리의 최소값
- 거리 = abs(r1-r2) + abs(c1-c2)
- 치킨거리: 집과 가장 가까운 치킨집 거리
- 도시의 치킨거리: sum(모든 집의 치킨거리)
- 아이디어:
    - 일단 폐업시키고 남은 치킨집의 모든 경우의 수를 구한다? => itertools.combinations(치킨집_리스트,M)
    - 각 경우의 수마다 도시의 치킨거리 를 구한다
    - 결과 중 도시의 치킨거리가 최소인 경우의 도시의 치킨거리를 반환한다
'''
from itertools import combinations
import sys

input = sys.stdin.readline

#풀이
def solution(n,m,graph):
    #치킨집과 집의 좌표를 모아둔 리스트 생성
    stores,houses = [],[]
    for r in range(n):
        for c in range(n):
            if graph[r][c] == 1:
                houses.append((r,c))
            elif graph[r][c] == 2:
                stores.append((r,c))
    
    #치킨집 폐업 경우의 수 구하기(조합)
    cases = list(combinations(stores,m))

    #남은 치킨집의 조합의 경우의 수마다 -> 각 집마다의 치킨거리 구하기 + 도시의 치킨거리 구하기
    res = []
    for case in cases:
        city_chicken_dist = 0
        for hr,hc in houses:
            chicken_dist = sys.maxsize
            for sr,sc in case:
                dist = abs(hr-sr) + abs(hc-sc)
                chicken_dist = min(chicken_dist, dist)
            city_chicken_dist += chicken_dist
        res.append(city_chicken_dist)

    return min(res)
        

#테스트케이스
n,m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

print(solution(n,m,graph))