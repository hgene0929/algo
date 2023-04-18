import sys

input = sys.stdin.readline

#풀이
def solution(nums):
    return sum(nums)

#테스트케이스
n = int(input())
nums = list(map(int, input().rstrip()))

print(solution(nums))