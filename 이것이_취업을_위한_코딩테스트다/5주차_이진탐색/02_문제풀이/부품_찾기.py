'''
구해야하는 것: 배열에 특정 원소가 속해있는지 여부 => 탐색 => 그런데 범위가 엄청 크고, 개수가 엄청 많아서 그냥 탐색(이중반복)하면 안됨 => 이진탐색 활용가능.
'''
import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline

#풀이
def count_element(na,target):
    left_idx = bisect_left(na,target)
    right_idx = bisect_right(na,target)
    cnt = right_idx - left_idx #na 리스트에서 target의 개수
    if cnt == 0:
        return "no"
    else:
        return "yes"

def solution(na,ma):
    result = []
    for target in ma:
        result.append(count_element(na,target))
    return result

#테스트케이스
n = int(input())
na = list(map(int, input().split()))
m = int(input())
ma = list(map(int, input().split()))

na.sort()
results = solution(na,ma)
for result in results:
    print(result,end=' ')