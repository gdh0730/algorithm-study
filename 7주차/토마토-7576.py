'''
Sudo 코드

1. 입력 처리
- 상자의 크기 M × N과 상자 상태를 입력받습니다.
- 익은 토마토의 위치를 미리 queue에 저장합니다.

2. BFS 탐색
- queue에 있는 모든 익은 토마토에서 시작하여 BFS 탐색을 수행합니다.
- 익은 토마토의 상하좌우에 위치한 익지 않은 토마토를 익히고, queue에 추가합니다.
- BFS 탐색이 끝나면 최소 일수가 계산됩니다.

3. 결과 계산
- 상자에 익지 않은 토마토가 남아 있으면 -1을 출력합니다.
- 모든 토마토가 익었다면 최소 일수를 출력합니다.

'''
from collections import deque

# BFS 함수 정의
def bfs(tomatoes, M, N):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:  # 익은 토마토 위치를 큐에 추가
                queue.append((i, j))
    
    # 이동 방향 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    days = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = 1  # 토마토를 익히고
                    queue.append((nx, ny))  # 큐에 추가
        days += 1  # 하루 증가
    
    # 익지 않은 토마토가 남아있는지 확인
    for row in tomatoes:
        if 0 in row:
            return -1
    return days - 1  # 시작 시 하루를 더했으므로 최종적으로 -1

# 입력 처리
M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

# BFS 수행 및 결과 출력
result = bfs(tomatoes, M, N)
print(result)
