'''
Sudo 코드
1. 입력 단계
- 정수 N을 입력받는다.

2. 초기화 단계
- 길이 N+1의 리스트 dp를 생성하고, 모든 값을 0으로 초기화한다.
- 초기 조건 설정:
    - dp[1] = 1
    - dp[2] = 1

3. 점화식을 이용한 DP 테이블 채우기
- 반복문을 통해 i = 3부터 N까지 다음 작업을 수행한다:
    - dp[i] = dp[i-1] + dp[i-2}

4. 출력 단계
- dp[N] 값을 출력한다.
'''
def pinary_number(N):
    # DP 테이블 초기화
    dp = [0] * (N + 1)
    
    # 초기 조건 설정
    dp[1] = 1
    if N > 1:
        dp[2] = 1
    
    # 점화식을 이용한 DP 테이블 채우기
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[N]

# 입력
N = int(input())
# 출력
print(pinary_number(N))
