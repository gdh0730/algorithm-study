'''
Sudo 코드
markdown
복사
편집
1. N 입력 (보드 크기)
2. K 입력 (사과 개수) → 사과 위치 저장
3. L 입력 (방향 전환 횟수) → 전환 시간/방향 저장

4. 초기 상태:
    - 뱀 위치: [(1, 1)] (deque)
    - 뱀 방향: 동쪽 (idx=0)

5. 시뮬레이션 시작:
    time = 0
    while True:
        1) 머리 이동 (현재 방향에 따라 이동)
        2) 벽 충돌 or 자기 몸과 충돌 시 종료
        3) 사과가 있으면:
            - 사과 제거
            - 몸 길이 증가
        4) 사과가 없으면:
            - 꼬리 줄이기
        5) time += 1
        6) time이 방향 전환 시간이라면 방향 변경

6. 종료 시 걸린 시간 출력
'''
from collections import deque

# 방향 벡터: 동(→), 남(↓), 서(←), 북(↑)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def simulate_game(n, apples, moves):
    # 보드 초기화
    board = [[0] * n for _ in range(n)]
    
    # 사과 배치
    for x, y in apples:
        board[x - 1][y - 1] = 1

    # 방향 전환 정보 저장
    turn_info = {}
    for time, direction in moves:
        turn_info[time] = direction

    # 뱀 초기 설정
    x, y = 0, 0  # 시작 위치
    board[x][y] = 2  # 뱀 표시
    snake = deque([(x, y)])
    direction_idx = 0  # 현재 방향 (동쪽)
    time = 0

    while True:
        time += 1
        # 다음 위치 계산
        dx, dy = directions[direction_idx]
        nx, ny = x + dx, y + dy

        # 1) 벽 충돌 or 자기 몸과 충돌 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
            break

        # 2) 이동 위치에 사과가 있는지 확인
        if board[nx][ny] == 1:  # 사과 있음
            board[nx][ny] = 2
            snake.append((nx, ny))
        else:  # 사과 없음 → 꼬리 줄이기
            board[nx][ny] = 2
            snake.append((nx, ny))
            # 꼬리 제거
            tx, ty = snake.popleft()
            board[tx][ty] = 0

        # 위치 업데이트
        x, y = nx, ny

        # 3) 방향 전환
        if time in turn_info:
            if turn_info[time] == 'L':
                direction_idx = (direction_idx - 1) % 4
            else:  # 'D'
                direction_idx = (direction_idx + 1) % 4

    return time


# 입력 처리
N = int(input())  # 보드 크기
K = int(input())  # 사과 개수
apples = [tuple(map(int, input().split())) for _ in range(K)]

L = int(input())  # 방향 전환 수
moves = [input().split() for _ in range(L)]
moves = [(int(x), c) for x, c in moves]

# 게임 시뮬레이션 수행
result = simulate_game(N, apples, moves)
print(result)
