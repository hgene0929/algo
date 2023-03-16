'''
[택배 배달과 수거하기]
- 아이디어: 
    - 한번에 최대한 멀리가서 작업을 최대한 적은 이동으로 마쳐버려야 한다 => 집을 뒤집어버린다(delievers,pickups 역순으로)
    - 한 번 갔을 때 cap 의 수량만으로 해결할 수 있다면 이동 더 할 필요 없다 => 남은 delievers,pickups 가 0이 될때까지 수량 빼주면 된다
    => 결정적인 아이디어 2가지:
        (1) 가장 거리가 먼 집부터 배달,수거 한다.
        (2) 배달해야할 개수, 수거해야할 개수 는 누적합으로 관리한다. <- 그래야 이동하는 중간에 배달,수거 하는 경우도 모두 고려할 수 있기 때문이다.
- 조심: 
    - 이동시 몇개의 택배상자를 들고갈지 고려하지 X -> 어차피 역순으로 뒤집고 나면 두번이동해도 괜찮다 -> 똑같다
    - 그냥 한번갔을때 남은 delievers와 pickups의 개수를 모두 caps(caps를 꽉 채워간다고 가정하고)로 뺴주고(갈 때 들고가서 내려놓고, 올 때 채워오면 되니까) 양수라면 다시 돌아갔다온다고 생각하면 된다
'''
#풀이
def solution(cap, n, deliveries, pickups):
    result = 0

    delivery,pickup = 0,0
    for i in range(n,0,-1): #최대한 먼 거리부터 이동하는 것이 이득(중간에 떨어뜨릴 수 있으니까) => 역순으로 확인
        delivery += deliveries[i-1] #i번째 집에 배달해야할 개수, 수거해야할 개수
        pickup += pickups[i-1]
        while delivery > 0 or pickup > 0: #배달해야할 개수와 수거해야할 개수가 모두 더이상 없을 때까지 창고 왔다갔다 해야한다
            delivery -= cap
            pickup -= cap
            result += i*2 #현재 집의 거리를 왕복하니까 현재집의 인덱스*2가 총 이동 거리
    
    return result

#테스트케이스
cap = 4 #트럭에 실을 수 있는 최대 택배상자 개수
n = 5 #집의 수
deliveries = [1, 0, 3, 1, 2] #각 집마다 배달할 상자 개수
pickups = [0, 3, 0, 4, 0] #각 집마다 수거할 상자 개수

print(solution(cap,n,deliveries,pickups))