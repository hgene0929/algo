'''
[무지의 먹방 라이브]
- 구해야하는 것: 1~N번 음식을 차례대로 1초씩 먹을 때, K+1초에 먹어야 할 음식 번호.
- 먹방 조건:
    - 음식은 주어진 순서대로 회전 => 다음 인덱스 = (현재인덱스 + 1) % N
    - 한번 먹으면 1초 소요 => 음식값 -= 1.
- 아이디어:
    - 일단 효율성 점수가 매겨진다 -> 최대한 효율성을 생각하면서 풀어야한다!
    - 음식을 반복하여 -1 하면서 K번 반복하더라도 20,000,000,000,000 -> 천억 훨씬 넘김 -> 안된다 이렇게 풀면!
    - 효율적인 아이디어:
        - len = len(food_times)인 경우, 1바퀴돌면 K - len이 될 것이다 -> n바퀴 돌면 K - n*len 이 될 것이다.
        - 이 와중에 음식값이 0이되면 리스트에서 빼주어야 한다 => 효율성을 고려하여 heapq 사용해볼 수 있을 것 같다.
        => 음식의 양을 기준으로 오름차순 정렬된 heapq에서 최소값(1st 원소값)만큼 회전을 반복했다고 가정하고 전체 음식의 양을 회전한 만큼 줄여준다 -> K가 될 때까지 반복.
'''
import heapq

#풀이
def solution(food_times, k):
    if sum(food_times) <= k: #시간에 비해 먹을 음식의 양이 부족 -> return -1
        return -1

    q = []
    for idx,food_time in enumerate(food_times):
        heapq.heappush(q,(food_time,idx)) #남은 음식의 양을 기준으로 오름차순 정렬: (남은 음식의 양, 음식의 인덱스)
    
    prev = 0 #이전에 먹어 없앴던 가장 작은 음식의 양(= 이전 회전횟수 = 여태까지 쓴 총 시간)
    remains = []

    while q:
        length = len(q) #남은 음식의 개수
        now = q[0][0] - prev #현재 먹어 없애야 할 가장 작은 음식의 양

        if now*length <= k: #가장 작은 양의 음식을 먹을 수 있을 때까지 회전 가능하다면 -> K초를 회전횟수*음식개수 만큼 빼준다
            heapq.heappop(q) #회전해서 먹어치워버린다
            k -= now * length #회전횟수 * 음식개수
            prev += now
        else: #이제 더이상 회전할 수 없다면 -> 그만 인덱스의 순서대로 음식을 먹을 순서를 지정한다
            break

    while q:
        remains.append(heapq.heappop(q)[1])
    remains.sort()

    return remains[k%len(remains)] + 1
        

#테스트케이스
food_times = [8,6,4]
k = 15

print(solution(food_times,k))