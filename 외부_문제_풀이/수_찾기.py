'''
구해야하는 것: N개의 정수 중 X라는 정수가 존재하는지 여부 출력
'''
import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline

#풀이
def binary_search(nums,target):
    left = bisect_left(nums,target)
    right = bisect_right(nums,target)
    return right-left

def solution(nums,finds):
    result = []
    for find in finds:
        if binary_search(nums,find) > 0:
            result.append(1)
        else:
            result.append(0)
    return result

#테스트케이스
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))
nums.sort()

results = solution(nums,finds)
for result in results:
    print(result)