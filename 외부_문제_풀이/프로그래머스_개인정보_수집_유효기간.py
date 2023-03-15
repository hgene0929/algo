'''
[개인정보 수집 유효기간]
- 전체 날짜단위를 하나로 통일하여 계산 => 제일 작은 단위로 통일 => 일수로
- 년 * 12 * 28, 월 * 28, 일
- enumerate() 함수 사용해서 인덱스까지 편리하게 사용
'''
#전체 날짜 단위를 "일"로 통일 => 더 큰 거 계산!!
def time_convert(t) :
    year, month, day = int(t.split('.')[0]),int(t.split('.')[1]),int(t.split('.')[2]) #map(int, t.split('.'))으로 간소화 가능
    return year * 12 * 28 + month * 28 + day #전체 날짜를 일 수로 변환

def solution(today, terms, privacies):
    term_dict = dict()
    today = time_convert(today)
    answer = []    
    
    for term in terms :
        name, period = term.split()
        term_dict[name] = int(period) * 28 #유효기간을 일수로 변환
    
    for idx, privacy in enumerate(privacies): #enumerate() 함수 통해서 인덱스까지 함께 추출
        start, name = privacy.split()
        end = time_convert(start) + term_dict[name]
        if end <= today :
            answer.append(idx+1)    
    
    return answer

#테스트케이스
today = "2020.01.01"#오늘 날짜
terms = ["Z 3", "D 5"] #약관종류, 유효기간(달)
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"] #정보를 받은 날짜, 약관의 종류

print(solution(today,terms,privacies))