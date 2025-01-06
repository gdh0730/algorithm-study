'''
Sudo 코드
1. 입력 단계
- n을 입력받는다. (직사각형의 길이)

2. 초기화 단계
- 길이 n+1의 리스트 dp를 생성하고, 모든 값을 0으로 초기화한다.
- 초기 조건을 설정한다:
    - dp[1] = 1  (2×1 크기의 직사각형을 채우는 방법은 한 가지)
    - dp[2] = 2  (2×2 크기의 직사각형을 채우는 방법은 두 가지)

3. 점화식을 이용한 DP 테이블 채우기
- 반복문을 통해 i = 3부터 n까지 다음 작업을 수행한다:
    - dp[i] = (dp[i-1] + dp[i-2]) % 10007(이때 10,007로 나눈 나머지를 저장하여 큰 수 계산을 방지)

4. 출력 단계
- dp[n] 값을 출력한다.
'''
def tiling_2n(n):
    # DP 테이블 초기화
    dp = [0] * (n + 1)
    
    # 초기 조건 설정
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    
    # DP 테이블 채우기
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    
    return dp[n]

# 입력
n = int(input())
# 출력
print(tiling_2n(n))
