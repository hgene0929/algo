'''
[이모티콘 할인행사]
- 목표: 
    1순위: 이모티콘 플러스 가입자 최대로 -> 이모티콘 가격의 합을 최대로 
    2순위: 이모티콘 판매 총액 최대로 -> 이모티콘 가격을 최대로
- 이모티콘 할인률 경우의 수: 10,20,30,40
- 아이디어: 
    - 사용자 최대 수 100, 할인 경우의 수 4, 이모티콘 종류 최대 7 => 완전탐색 가능할듯?
    - 각 이모티콘 집합 * 할인률 집합 => 각 경우의 수마다 이모티콘 플러스 가입자 수, 이모티콘 구매 총비용 계산해서 정답 구하기?
     - 곱집합 구하는 라이브러리 itertools.product(li1,li1, ..., repeat=중복포함(생성길이))
'''
from itertools import product

def get_discount(price,discount):
    return price - int(price * discount / 100) #할인적용시, 조건에 따라 가격은 100의 배수이기 때문에 정수형으로 변환해도 누락 X

#풀이: 이모티콘 * 할인률 곱집합을 구하여 각 경우의 수마다의 결과를 계산해서 최적의 값을 구한다
def solution(users, emoticons):
    discounts = list(product([10,20,30,40], repeat=len(emoticons))) #곱집합 구하기 -> 이모티콘 별로 할인율을 적용할 수 있는 모든 경우의 수 구했다

    max_cnt,max_price = 0,0

    for discount in discounts:
        temp_cnt,temp_price = 0,0
        for user in users:
            price_per_user = 0
            for idx,emoticon in enumerate(emoticons):
                if user[0] <= discount[idx]:
                    price_per_user += get_discount(emoticon,discount[idx]) #사용자가 정해놓은 할인율보다 높은 이모티콘 구매 -> 비용추가했다
            if price_per_user >= user[1]:
                temp_cnt += 1 #사용자가 정해놓은 금액보다 높은 비용 -> 플러스 가입했다 -> 이모티콘 플러스 가입 O & 이모티콘 전체 결제 X
            else:
                temp_price += price_per_user #이모티콘 플러스 가입 X & 이모티콘 전체 결제 O

        if max_cnt < temp_cnt:
            max_cnt,max_price = temp_cnt,temp_price #우선순위 1번: 플러스 가입자 높으면 갱신
        elif max_cnt == temp_cnt:
            if max_price < temp_price:
                max_cnt,max_price = temp_cnt,temp_price #우선순위 2번: 플러스 가입자 수 같다면, 총 구매비용 높으면 갱신

    return [max_cnt,max_price]

#테스트케이스
users = [[40, 10000], #이모티콘 구매 할인율, 이모티콘 플러스 가입 이모티콘 총비용
         [25, 10000]]
emoticons = [7000, 9000]

print(solution(users,emoticons))