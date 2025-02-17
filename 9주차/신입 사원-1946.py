'''
Sudo 코드
1. 테스트 케이스 개수 T를 입력받는다.
2. T번 반복하면서 다음을 수행한다:
   1. 지원자 수 N을 입력받는다.
   2. N명의 (서류 순위, 면접 순위)를 입력받아 리스트 applicants에 저장한다.
   3. applicants 리스트를 "서류 순위" 기준으로 오름차순 정렬한다.
   4. 첫 번째 지원자는 무조건 선발 (선발자 수 count = 1)
   5. 현재까지의 최소 면접 순위(min_interview)를 첫 번째 지원자의 면접 순위로 설정한다.
   6. 두 번째 지원자부터 N번째 지원자까지 반복하며:
      - 현재 지원자의 면접 순위가 min_interview보다 낮으면:
        - 선발하고 count 증가
        - min_interview 갱신
   7. 최종 count 값을 출력한다.
'''
import sys

def max_hires(N, applicants):
    # 서류 심사 순위를 기준으로 정렬
    applicants.sort()
    
    count = 1  # 첫 번째 지원자는 무조건 선발
    min_interview = applicants[0][1]  # 첫 번째 지원자의 면접 순위
    
    # 두 번째 지원자부터 탐색
    for i in range(1, N):
        if applicants[i][1] < min_interview:  # 면접 순위가 더 낮으면 선발 가능
            count += 1
            min_interview = applicants[i][1]  # 최소 면접 순위 갱신

    return count

# 입력 처리
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    applicants = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    # 결과 출력
    print(max_hires(N, applicants))
