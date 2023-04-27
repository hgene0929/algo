'''
주어진 것: 정렬하는 기준에 우선순위가 있다.
정렬 우선순위: 국어 내림차순 > 영어 오름차순 > 수학 내림차순 > 이름 알파벳순.
아이디어: sort() 함수의 key lamda를 사용하여 정렬의 우선순위를 나열한다.
'''
import sys

input = sys.stdin.readline

#풀이
def solution(students):
    students.sort(key=lambda x:[-int(x[1]), int(x[2]), -int(x[3]), x[0]])
    results = []
    for student in students:
        results.append(student[0])
    return results

#테스트케이스
n = int(input())
students = [list(map(str, input().rstrip().split())) for _ in range(n)]

results = solution(students)
for result in results:
    print(result)