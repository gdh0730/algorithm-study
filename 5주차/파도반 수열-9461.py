'''
Sudo 코드
1. 입력 단계
- 테스트 케이스 수 T를 입력받는다.
- 각 테스트 케이스에 대해 N 값을 입력받아 리스트에 저장한다.

2. 초기화 단계
- dp 리스트를 길이 101로 초기화하고, 모든 값을 0으로 설정한다.
- 초기 조건으로 dp[1]부터 dp[5]까지 각각 1, 1, 1, 2, 2로 설정한다.

3. DP 테이블 채우기 단계
- 반복문을 통해 n=6부터 최대 N까지 다음 점화식을 이용하여 dp 테이블을 채운다:
    dp[n] = dp[n−1] + dp[n−5]

4. 출력 단계
- 각 테스트 케이스에 대해 dp[N] 값을 출력한다.
'''
def padovan_sequence(max_n=100):
    # DP 테이블 초기화
    dp = [0] * (max_n + 1)
    
    # 초기 조건 설정
    dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
    
    # 점화식에 따라 DP 테이블 채우기
    for n in range(6, max_n + 1):
        dp[n] = dp[n - 1] + dp[n - 5]
    
    return dp

def solve_padovan_problem():
    T = int(input())  # 테스트 케이스 수 입력
    queries = [int(input()) for _ in range(T)]  # 각 테스트 케이스 입력
    
    # 파도반 수열 미리 계산
    dp = padovan_sequence()
    
    # 각 테스트 케이스에 대해 결과 출력
    for n in queries:
        print(dp[n])

# 실행
if __name__ == "__main__":
    solve_padovan_problem()
