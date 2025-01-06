'''
Sudo 코드
1. 입력 단계
- T를 입력받는다. (테스트 케이스의 개수)
- queries 리스트에 각 테스트 케이스 값을 입력받는다.

2. 초기화 단계
- count_zero 리스트와 count_one 리스트를 길이 41로 생성하고, 모든 값을 0으로 초기화한다.
- count_zero[0]에 1을 저장하고, count_one[0]에 0을 저장한다.
(즉, fibonacci(0) 호출 시 0이 1번 출력되고, 1은 출력되지 않음)
- count_zero[1]에 0을 저장하고, count_one[1]에 1을 저장한다.
(즉, fibonacci(1) 호출 시 1이 1번 출력되고, 0은 출력되지 않음)

3. DP 테이블 채우기 단계
- 반복문을 통해 n = 2부터 40까지 다음 작업을 수행한다:
    - count_zero[n]을 count_zero[n-1] + count_zero[n-2]로 계산하여 저장한다.
    - count_one[n]을 count_one[n-1] + count_one[n-2]로 계산하여 저장한다.

4. 출력 단계
- 각 테스트 케이스 n에 대해:
    - count_zero[n]과 count_one[n] 값을 공백으로 구분하여 출력한다.
'''
def fibonacci_counts(max_n=40):
    # 최대 N까지의 0과 1 출력 횟수를 저장할 리스트
    count_zero = [0] * (max_n + 1)
    count_one = [0] * (max_n + 1)
    
    # 초기 조건 설정
    count_zero[0] = 1
    count_one[0] = 0
    count_zero[1] = 0
    count_one[1] = 1
    
    # DP 테이블 채우기
    for n in range(2, max_n + 1):
        count_zero[n] = count_zero[n - 1] + count_zero[n - 2]
        count_one[n] = count_one[n - 1] + count_one[n - 2]
    
    return count_zero, count_one

def solve_fibonacci_problem():
    T = int(input())  # 테스트 케이스 수 입력
    queries = [int(input()) for _ in range(T)]  # 각 테스트 케이스 입력
    
    # 0과 1의 출력 횟수를 미리 계산
    count_zero, count_one = fibonacci_counts()
    
    # 각 테스트 케이스에 대해 결과 출력
    for n in queries:
        print(count_zero[n], count_one[n])

# 실행
if __name__ == "__main__":
    solve_fibonacci_problem()
