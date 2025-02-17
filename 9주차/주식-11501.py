'''
Sudo 코드
1. 입력으로 테스트 케이스 개수 T를 받는다.
2. T번 반복하면서 다음을 수행한다:
    1. 날의 수 N을 입력받는다.
    2. N개의 주가 정보를 리스트로 저장한다.
    3. max_price를 0으로 초기화하고, total_profit을 0으로 초기화한다.
    4. 주가 리스트를 **뒤에서부터 순회**하면서:
        - 현재 가격이 max_price보다 크면 max_price를 갱신한다.
        - 그렇지 않으면, max_price에서 현재 가격을 뺀 값만큼 이익을 추가한다.
    5. total_profit을 출력한다.
'''
import sys

def max_profit(prices):
    max_price = 0
    total_profit = 0
    
    # 뒤에서부터 탐색
    for price in reversed(prices):
        if price > max_price:
            max_price = price  # 최대 가격 갱신
        else:
            total_profit += max_price - price  # 차익 계산
    
    return total_profit

# 입력 처리
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    prices = list(map(int, sys.stdin.readline().strip().split()))
    print(max_profit(prices))
