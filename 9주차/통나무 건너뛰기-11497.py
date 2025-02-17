'''
Sudo 코드
1. 테스트 케이스 개수 T를 입력받는다.
2. T번 반복하며:
   1. 통나무 개수 N을 입력받는다.
   2. 통나무 높이 리스트 L을 입력받는다.
   3. L을 오름차순 정렬한다.
   4. 정렬된 L을 새 리스트 new_L에 번갈아가며 배치한다. (작은 값부터 왼쪽, 오른쪽 순으로)
   5. new_L에서 인접한 원소의 차이의 최댓값을 계산하여 출력한다.

- 정렬 → [2, 4, 5, 7, 9]
- 지그재그 배치 → [2, 5, 9, 7, 4]
'''
import sys

def min_difficulty(N, heights):
    heights.sort()  # 높이를 오름차순 정렬
    arranged = [0] * N  # 결과 리스트
    left, right = 0, N - 1  # 좌우 배치 인덱스
    
    # 번갈아가며 양쪽으로 배치
    for i in range(N):
        if i % 2 == 0:
            arranged[left] = heights[i]
            left += 1
        else:
            arranged[right] = heights[i]
            right -= 1
    
    # 난이도 계산 (최대 높이 차이)
    max_diff = max(abs(arranged[i] - arranged[i+1]) for i in range(N-1))
    max_diff = max(max_diff, abs(arranged[0] - arranged[-1]))  # 원형 고려

    return max_diff

# 입력 처리
T = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 통나무 개수
    heights = list(map(int, sys.stdin.readline().split()))  # 통나무 높이 리스트
    print(min_difficulty(N, heights))
