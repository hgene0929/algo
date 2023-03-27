'''
[자물쇠와 열쇠]
- 문 여는 조건:
    - 자물쇠 홈 + 열쇠 돌기 -> O
    - 자물쇠 돌기 + 열쇠 돌기 -> X
    - 자물쇠 홈 + 열쇠 홈 -> X
    - 영역 벗어날 수 있음
- 열쇠 이동: 
    - 회전: 
        - 헷갈리니까 시계방향 한방향으로만
        - rotate 점화식: (x1,y1) -> (y1,len-1-x1)
    - 이동: moves = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우 한칸씩
- 아이디어: 
    - 자물쇠는 가만히 두고, 그 위에서 열쇠만 이동+회전?
    - 자물쇠 범위를 벗어날 수 있음?
    => 그럼 자물쇠의 범위를 확장시켜서 그 안에서 열쇠가 일일이 움직여보면? 자물쇠범위는 얼마나? -> 열쇠 최대 크기만큼 늘려보면? -> 자물쇠가 완전히 가운데 배치 안됨
    => 자물쇠_길이 = 자물쇠_길이 + (열쇠_길이-1)*2 <- 열쇠가 적어도 자물쇠와 1겹은 겹치면서.. 범위 안에 다 들어갈 수 있음..?!
- 표현:
    - 자물쇠 홈: -1
    - 자물쇠 돌기: 1
    - 열쇠 홈: 0
    - 열쇠 돌기: 1
    => 문이 안열리는 경우: 확장된 자물쇠에 -1이 존재하거나, 2가 존재하는 경우!
'''
#풀이
def rotate(a): #시계방향으로 90도 회전한 리스트 반환(회전함수)
    row_length,col_length = len(a),len(a)
    ra = [[0]*row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            ra[c][row_length-r-1] = a[r][c]
    return ra

#더 간단하게 90도 시계방향 회전 구현
def rotate_simple(a):
    return list(zip(*a[::-1]))

def solution(key, lock):
    #1. 자물쇠의 범위를 넓혀서 열쇠&자물쇠가 겹치지 않는 부분까지도 고려한다
    key_length,lock_length = len(key),len(lock)
    temp_length = lock_length + (key_length-1)*2
    temp = [[1]*temp_length for _ in range(temp_length)]
    for r in range(key_length):
        for c in range(key_length):
            temp[r+key_length-1][c+key_length-1] = lock[r][c]

    #2. 열쇠를 temp[0][0] ~ temp[temp_length-key_length][temp_length-key_length] 까지 넣어서 회전,이동 하면서 맞춰지는지 확인 => temp의 2,0인 값이 존재하면 X
    row,col,cnt_rotate = 0,0,0
    while True:
        #2-1) 열쇠와 자물쇠 대조(딱 맞으면 모든 칸의 값이 1)
        for r in range(key_length):
            for c in range(key_length):
                temp[row+r][col+c] += key[r][c]

        #2-2) 열쇠-자물쇠 딱 맞는지 확인
        is_possible = True
        for r in range(lock_length):
            for c in range(lock_length):
                if temp[r+key_length-1][c+key_length-1] == 0 or temp[r+key_length-1][c+key_length-1] == 2:
                    is_possible = False
                    break
        
        if is_possible:
            return True
        
        #2-3) 안맞으면 원복
        for r in range(key_length):
            for c in range(key_length):
                temp[row+r][col+c] -= key[r][c]

        #2-4) 같은 자리에서 회전 4번 했으면 -> 이동, 아니면 -> 회전
        if cnt_rotate == 4:
            if col == temp_length-key_length:
                if row == temp_length-key_length:
                    return False
                else:
                    row += 1
                    col = 0
            else:
                col += 1
            cnt_rotate = 0
        else:
            key = rotate(key)
            cnt_rotate += 1


#테스트케이스
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))