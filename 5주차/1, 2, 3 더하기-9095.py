'''
Sudo 코드드
1. 입력 단계
- 테스트 케이스 수 T를 입력받는다.
- 각 테스트 케이스에 대해 정수 n을 입력받아 queries 리스트에 저장한다.

2. 초기화 단계
- 최대 n = 10까지의 값을 계산하기 위해 길이 11의 리스트 dp를 생성하고, 모든 값을 0으로 초기화한다.
- 초기 조건을 설정한다:
    - dp[1] = 1 (1을 만드는 방법은 [1] 한 가지)
    - dp[2] = 2 (2를 만드는 방법은 [1+1, 2] 두 가지)
    - dp[3] = 4 (3을 만드는 방법은 [1+1+1, 1+2, 2+1, 3] 네 가지)

3. 점화식을 이용한 DP 테이블 채우기
- 반복문을 통해 i = 4부터 10까지 다음 작업을 수행한다:
    - dp[i] = dp[i-1] + dp[i-2] + dp[i-3}(각각 마지막에 1, 2, 3을 더하는 경우로 분할)

4. 출력 단계
- 각 테스트 케이스에 대해 dp[n] 값을 출력한다.
'''
def count_ways_to_sum(max_n=10):
    # DP 테이블 초기화
    dp = [0] * (max_n + 1)
    
    # 초기 조건 설정
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    # 점화식을 이용해 DP 테이블 채우기
    for i in range(4, max_n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp

def solve_sum_problem():
    T = int(input())  # 테스트 케이스 수 입력
    queries = [int(input()) for _ in range(T)]  # 각 테스트 케이스 입력
    
    # 1부터 10까지의 방법의 수 미리 계산
    dp = count_ways_to_sum()
    
    # 각 테스트 케이스에 대해 결과 출력
    for n in queries:
        print(dp[n])

# 실행
if __name__ == "__main__":
    solve_sum_problem()
