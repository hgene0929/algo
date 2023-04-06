'''
구해야하는 것: 가지고 있는 숫자 N개 중 주어진 M개의 정수를 몇개 가지고 있는지 출력
아이디어:
    - N개의 숫자 중에서 M개의 정수를 각각 탐색하여 개수 세기 -> 탐색
    - 근데 입력값이 매우 큼 -> 순차탐색 X -> 이진탐색 O
'''
import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline

#풀이
def search_cnt(numbers,target): #bisect 라이브러리 활용하여 중복되는 정수의 개수를 리스트에서 도출(범위를 도출해내는 것과 동일)
    left = bisect_left(numbers,target)
    right = bisect_right(numbers,target)
    return right - left

def solution(numbers,targets):
    result = []
    numbers.sort() #이진탐색을 위해 대상이 되는 리스트 정렬
    for target in targets:
        cnt = search_cnt(numbers,target)
        result.append(cnt)
    return result

#테스트케이스
n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

results = solution(numbers,targets)
for result in results:
    print(result, end=' ')