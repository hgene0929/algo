'''
[게임 개발]
- N * M 맵에서 캐릭터가 이동가능한 칸의 개수(결국 더이상 움직일 수 없을 때까지 이동하면서 누적합 +1씩한 값) 구하기
- 이동하는 조건 :
    - L > D > R > U => 이동가능 = [(0,-1),(1,0),(0,1),(-1,0)] => 4가지를 반복하면서 (언제까지? -> 전진할 수 있을 때까지)
        - 근데 여기서 방향이 북쪽 0, 동쪽 1, 남쪽 2, 서쪽 3 으로 주어지니까 이 인덱스에 맞에 해두고 반복 돌면 될듯?
    - 전진할 수 있으면 전진 (없으면? -> 뒤가 바다인지 확인 -> 바다 아니면? -> 현재 방향에서 뒤로 한칸 | 바다면? -> 종료)
- 전진할 수 없는 경우 : 4칸이 모두 가본 칸이거나 바다(or 맵 범위 벗어남)
'''
import sys

input = sys.stdin.readline

#입력
n,m = map(int, input().split())
x,y,d = map(int, input().split()) #x,y = 현재 캐릭터 위치 좌표 | d = 방향
map = [list(map(int, input().rstrip().split())) for _ in range(n)]

#풀이 : 구현 => 주어진 조건대로 이동시키면서 누적만 시킬 것
cnt = 0
moves = [(-1,0),(0,1),(1,0),(0,-1)]
cnt_impossible = 0
map[x][y] = 2

while True:
    if cnt_impossible == 4: #(4) 4방향 모두 전진불가능한 경우 : 뒷칸이 바다인지 확인
        cnt_impossible = 0
        nd = (d+2)%4 #현재 방향을 기준으로 뒤쪽이 어디인지 확인(회전을 할 것은 아니므로 d에 누적은 X)
        nx,ny = x+moves[nd][0],y+moves[nd][1]
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 1: #맵 범위 내에 있고, 바다가 아니면 => 뒤로 한 칸 이동
            cnt += 1
            x,y = nx,ny
            map[x][y] = 2
        else:
            break #뒤칸이 바다인경우(맵 범위를 벗어나는 경우 포함)
    
    d = (d-1)%4 #(1)현재 방향에서 왼쪽으로 90도 회전 : (현재인덱스-1)%리스트크기 => 왼쪽방향으로 현재 리스트 원소 반복
    nx,ny = x+moves[d][0],y+moves[d][1]
    if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0: #(2)앞으로 전진가능한 경우 : 맵의 범위내에 있고, 육지(이미 가본 칸은 2로 표시할 것임)
        cnt_impossible = 0
        cnt += 1 #가본 칸 += 1
        x,y = nx,ny #이동 => 현재좌표 갱신
        map[x][y] = 2 #이미 가본 칸임을 표시
    else:
        cnt_impossible += 1 #(3)앞으로 전진불가능한 경우 : 다른 방향도 확인

#출력
print(cnt)