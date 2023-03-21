'''
[문자열 재정렬]
- 구해야하는 것: S 에서 알파벳은 오름차순으로 정렬 + 숫자는 합 구함.
- 아이디어: 
    - 일일이 대조해보면서 알파벳 -> 정렬, 숫자 -> 더하기.
    - 문자열이 알파벳인지, 숫자인지 확인하는 메서드 => isalpha(), isdigit()
'''
#입력
strings = input()

#풀이
nums = 0
strs = []

for string in strings:
    if string.isdigit():
        nums += int(string)
    else:
        strs.append(string)

strs.sort()
result = ''
if nums == 0:
    result = ''.join(strs)
else:
    result = ''.join(strs) + str(nums)

#출력
print(result)