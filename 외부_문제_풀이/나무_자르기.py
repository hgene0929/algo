'''
- 구해야하는 것: 적어도 M미터의 나무를 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값
- 절단기 작동 원리:
    - 나무는 세로 1줄로 놓여있다
    - 절단기의 높이보다 긴 나무 - 절단기 높이 만큼이 각 나무에서 얻을 수 있는 미터
    - 절단기의 높이 >= 0
- 아이디어:
    - 일단 나무의 수, 나무의 길이 겁나 크다 -> 일반적으로 반복문 한번이라도 돌리면 X
    - 절단기의 높이를 이진탐색으로 찾는 것이 가장 효율적일 것
'''
import sys

input = sys.stdin.readline

#풀이
def solution(trees,target,start,end):
    result = 0
    while start <= end:
        total = 0
        mid = (start+end)//2 #이진탐색 중 설정한 임시 절단기 길이
        for tree in trees: #나무를 잘라서 총 길이를 확인해봄
            if tree > mid:
                total += tree - mid
        if total < target: #총 길이가 M미터보다 작으면 -> 절단기 길이 줄여야 함
            end = mid - 1
        else:
            result = mid #총 길이가 M미터보다 크거나 같으면 -> 절단기 길이 최대한 늘려본다
            start = mid + 1
    return result

#테스트케이스
n,m = map(int, input().split())
trees = list(map(int, input().rstrip().split()))

print(solution(trees,m,0,max(trees)))