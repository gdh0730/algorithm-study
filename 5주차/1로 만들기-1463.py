'''
[Sudo 코드]
점화식 : dp[i]=min(dp[i−1]+1, dp[i//2]+1 (if i%2==0), dp[i//3]+1 (if i%3==0))

1. 입력 단계
- 정수 N을 입력받는다.

2. 초기화 단계
- 길이 N+1의 리스트 dp를 생성하고, 모든 값을 0으로 초기화한다.
- 초기 조건 설정:
    - dp[1] = 0

3. 점화식을 이용한 DP 테이블 채우기
- 반복문을 통해 i = 2부터 N까지 다음 작업을 수행한다:
    - dp[i] = dp[i-1] + 1 (1을 빼는 연산)
    - 만약 i가 2로 나누어 떨어지면,
        dp[i] = min(dp[i], dp[i//2] + 1) (2로 나누는 연산과 비교하여 최소값 선택)
    - 만약 i가 3으로 나누어 떨어지면,
        dp[i] = min(dp[i], dp[i//3] + 1) (3으로 나누는 연산과 비교하여 최소값 선택)

4. 출력 단계
- dp[N] 값을 출력한다.
'''
def min_operations_to_one(N):
    # DP 테이블 초기화
    dp = [0] * (N + 1)
    
    # DP 테이블 채우기
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1  # 1을 빼는 연산
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)  # 2로 나누는 연산
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)  # 3으로 나누는 연산

    return dp[N]

# 입력
N = int(input())
# 출력
print(min_operations_to_one(N))
