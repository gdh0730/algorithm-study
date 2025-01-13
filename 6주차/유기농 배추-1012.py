'''
Sudo 코드

1. 입력 처리 단계
- 테스트 케이스 수 T를 입력받는다.
- 각 테스트 케이스에 대해 배추밭의 크기 M x N과 배추의 개수 K, 그리고 배추가 심어진 위치를 입력받아 2차원 격자판을 생성한다.

2. DFS 또는 BFS 탐색 단계
- 격자판을 탐색하며 배추가 심어진 위치(1)를 찾고, 방문하지 않은 배추에 대해 DFS 또는 BFS 탐색을 수행하여 해당 군집을 방문 처리한다.
- 새로운 탐색이 시작될 때마다 군집의 수를 1 증가시킨다.

3. 출력 단계
- 각 테스트 케이스에 대해 구한 군집의 수(배추흰지렁이 수)를 출력한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

# BFS 함수 정의
def bfs(x, y, graph, visited, M, N):
    queue = deque([(x, y)])
    visited[x][y] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우 방향
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

# 입력 처리
T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().strip().split())
    graph = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    
    # 배추 위치 입력
    for _ in range(K):
        X, Y = map(int, input().strip().split())
        graph[X][Y] = 1
    
    worm_count = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:  # 방문하지 않은 배추
                bfs(i, j, graph, visited, M, N)
                worm_count += 1  # 새로운 군집 발견
    
    # 결과 출력
    print(worm_count)
