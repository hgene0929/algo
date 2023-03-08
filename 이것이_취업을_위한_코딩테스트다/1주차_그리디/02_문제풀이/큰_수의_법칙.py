'''
[큰 수의 법칙]
- 구해야 하는 것 : 주어진 수의 배열을 M번 더하여 나올 수 있는 최댓값
- 조건 : 같은 인덱스의 숫자는 연속해서 K번을 초과하여 더해질 수 없다
- 아이디어 : 수를 정렬하여 가장 큰 수의 값을 K번 더하고, 그다음 작은 수의 값을 1번 더하는 과정을 K+1이 M이 될 때까지 반복하면 되지 않을까 => 효율성에서 감점되지 않도록 주의하면서 풀어보기(이중반복문 최대한 피해보기)
'''
#입력 
n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

#풀이
nums.sort(reverse=True)

first = nums[0]
second = nums[1]

#핵심 : k+1 패턴을 가지고 반복되니까, m//(k+1)은 패턴(가장 큰 수를 k번 더하고 그다음수을 1번 더하는 것)이 반복가능한 횟수 -> 여기에 k번 곱하고, m % (k+1)은 패턴이 다 끝나기 전이므로 모두 가장 큰 수의 계산 -> 이를 모두 더하면 가장 큰 수의 연산가능횟수
fisrt_cnt = m//(k+1)*k + m%(k+1)
second_cnt = m - fisrt_cnt

result = first*fisrt_cnt + second*second_cnt

#출력
print(result)