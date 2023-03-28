'''
[기둥과 보 설치]
- 구해야하는 것: 
- 조건:
    - 기둥(x,y):
        1. 바닥 위 => y == 0
        2. 보의 한쪽 끝 부분 위 => (x,y) == 보 or (x-1,y) == 보
        3. 다른 기둥 위 => (x,y-1) == 기둥
    - 보(x,y):
        1. 한쪽 끝 부분이 기둥 위 => (x,y-1) == 기둥 or (x+1,y-1) == 기둥
        2. 양쪽 끝 부분이 다른 보와 동시에 연결 => (x-1,y) == 보 and (x+1,y) == 보
- 입력: [x,y,a,b] == [가로 좌표, 세로 좌표, 0은 기둥 1은 보, 0은 삭제 1은 설치]
- 출력: [x,y,a] == [가로 좌표, 세로 좌표, 0은 기둥 1은 보]

** 사실, 삭제의 경우에는 여파의 범위가 넓고 고려사항이 복잡해서 그냥 함수로 전체 다 한 번 훑는다지만,,
   설치는 고려할 부분이 적어서 아래와 같이 함수로 풀면 시간은 더 걸릴듯.. 근데 일단 현재 문제에서는 시간이 가능해서 그렇게 풀었음.
'''
#풀이
def is_possible(arr): #현재 상태가 성립가능한지 확인하는 함수
    for x,y,a in arr:
        if a == 0: #기둥
            if y == 0: #바닥위
                continue
            elif [x,y,1] in arr or [x-1,y,1] in arr: #보의 한쪽 끝 부분위
                continue
            elif [x,y-1,0] in arr: #다른 기둥위
                continue
            return False
        else: #보
            if [x,y-1,0] in arr or [x+1,y-1,0] in arr:
                continue
            elif [x-1,y,1] in arr and [x+1,y,1] in arr:
                continue
            return False
    return True

def solution(n, build_frame):
    res = []

    for x,y,a,b in build_frame:
        if a == 0 and b == 0: #기둥-삭제
            res.remove([x,y,a])
            if not is_possible(res):
                res.append([x,y,a])
        elif a == 0 and b == 1: #기둥-설치
            res.append([x,y,a])
            if not is_possible(res):
                res.remove([x,y,a])
        elif a == 1 and b == 0: #보-삭제
            res.remove([x,y,a])
            if not is_possible(res):
                res.append([x,y,a])
        else: #보-설치
            res.append([x,y,a])
            if not is_possible(res):
                res.remove([x,y,a])

    res.sort(key=lambda x:(x[0],x[1],x[2]))
    return res


#테스트케이스
n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

print(solution(n, build_frame))