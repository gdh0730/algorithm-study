'''
Sudo 코드
1. 입력 받기: N, 재료 리스트(신맛 S, 쓴맛 B)
2. 최소 차이 diff = 무한대로 설정
3. 부분집합을 생성하여 다음 수행:
    - 선택된 재료가 하나 이상이면:
        - 신맛 = 선택된 재료들의 S의 곱
        - 쓴맛 = 선택된 재료들의 B의 합
        - diff = min(diff, |신맛 - 쓴맛|)
4. diff를 출력
'''
from itertools import combinations

# 입력 처리
N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]

# 결과 초기화
min_diff = float('inf')

# 부분집합 생성
for i in range(1, N + 1):
    for subset in combinations(ingredients, i):
        s, b = 1, 0  # 신맛(곱), 쓴맛(합)
        for ing in subset:
            s *= ing[0]  # 신맛 곱
            b += ing[1]  # 쓴맛 합
        min_diff = min(min_diff, abs(s - b))

# 결과 출력
print(min_diff)
