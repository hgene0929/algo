'''
[럭키 스트레이트]
- 럭키 스트레이트 달성 조건: 현재 캐릭터 점수 N을 자릿수 기준으로 반띵 -> 왼쪽 자릿수의 합 == 오른쪽 자릿수의 합.
- 구해야하는 것: 주어진 점수가 럭키 스트레이트 사용가능한 점수인지 여부.
- 아이디어:
    - 점수 N은 항상 짝의 자릿수 -> 반띵의 기준이 되는 자리는 => len(N) // 2 
    - 비교대상은 => N[:len(N)//2] ?? N[len(n)//2:]
    - N은 최대 8자리수, 분할하면 최대 4자리씩 => SUM() 사용해도 무방 
'''
#입력
nums = list(map(int, input()))

#풀이
target = len(nums)//2

left = nums[:target]
right = nums[target:]

#출력
if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')