'''
Sudo 코드

1. 입력 처리
- 총 층수 F, 현재 층 S, 목표 층 G, 한 번에 올라가는 층수 U, 한 번에 내려가는 층수 D를 입력받습니다.

2. BFS 탐색
- queue를 이용하여 BFS를 수행합니다.
- 시작 위치 S를 queue에 추가하고 방문 배열을 초기화합니다.
- queue에서 현재 층을 꺼내고, 가능한 다음 이동(위로 U층, 아래로 D층)을 계산합니다.
- 이동할 층이 건물 범위 내에 있고 방문하지 않았다면 큐에 추가하고, 버튼을 누른 횟수를 갱신합니다.
- 목표 층 G에 도달하면 버튼 누른 횟수를 출력합니다.

3. 결과 출력
- BFS 탐색이 끝날 때까지 G층에 도달하지 못하면 **"use the stairs"**를 출력합니다.
'''
from collections import deque

def bfs(F, S, G, U, D):
    queue = deque([S])  # BFS를 위한 큐
    visited = [-1] * (F + 1)  # 방문 여부 및 버튼 횟수 저장, -1은 미방문
    visited[S] = 0  # 시작 위치의 버튼 횟수는 0

    while queue:
        current = queue.popleft()

        # 목표 층에 도달하면 버튼 횟수 반환
        if current == G:
            return visited[current]

        # 위로 U층 이동
        if current + U <= F and visited[current + U] == -1:
            queue.append(current + U)
            visited[current + U] = visited[current] + 1

        # 아래로 D층 이동
        if current - D >= 1 and visited[current - D] == -1:
            queue.append(current - D)
            visited[current - D] = visited[current] + 1

    return "use the stairs"  # G층에 도달하지 못한 경우

# 입력 처리
F, S, G, U, D = map(int, input().split())

# BFS 수행 및 결과 출력
print(bfs(F, S, G, U, D))
