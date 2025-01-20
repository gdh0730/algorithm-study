'''
Sudo 코드

1. 입력 처리
- 미로의 크기 N × M과 미로 배열을 입력받아 maze 리스트에 저장합니다.
- 미로의 값이 1인 칸은 이동 가능, 0인 칸은 이동 불가능합니다.

2. BFS 탐색
- queue는 BFS 탐색에서 방문할 노드를 저장합니다.
- 시작점 (0, 0)에서 BFS를 시작하며, 상하좌우로 이동 가능한 칸을 탐색합니다.
- 탐색 시 방문한 칸의 값을 현재 칸까지의 거리로 갱신합니다.
- 도착점 (N-1, M-1)에 도달하면 BFS를 종료하고 최단 거리를 반환합니다.

3. 결과 출력
- BFS 탐색이 끝나면 도착점 (N-1, M-1)에 저장된 최단 거리를 출력합니다.
'''
from collections import deque

# BFS 함수 정의
def bfs(maze, N, M):
    # 이동 방향 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])  # 시작점 추가
    maze[0][0] = 1  # 시작점 거리 설정

    while queue:
        x, y = queue.popleft()

        # 목적지 도달 시 거리 반환
        if x == N - 1 and y == M - 1:
            return maze[x][y]

        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 미로 범위 내에서 이동 가능하고, 방문하지 않은 칸
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 거리 갱신
                queue.append((nx, ny))

# 입력 처리
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

# BFS 수행 및 결과 출력
print(bfs(maze, N, M))
