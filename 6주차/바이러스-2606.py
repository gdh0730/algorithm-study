'''
Sudo 코드

1. 그래프 입력 처리
- 컴퓨터 수 N과 간선 수 M을 입력받는다.
- M개의 간선 정보를 입력받아 무방향 그래프를 인접 리스트로 생성한다.

2. DFS 또는 BFS 탐색 함수 정의
- 1번 컴퓨터부터 시작하여 연결된 모든 컴퓨터를 탐색한다.
- 방문한 컴퓨터를 기록하기 위해 방문 배열을 사용한다.

3. 탐색 후 결과 출력
- 탐색한 컴퓨터의 개수에서 1번 컴퓨터 자신을 제외한 개수를 출력한다.
'''
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += 1  # 방문한 컴퓨터 수 증가
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    return count - 1  # 1번 컴퓨터 자신 제외

# 입력 처리
N = int(input())  # 컴퓨터 수
M = int(input())  # 간선 수
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 배열 초기화
visited = [False] * (N + 1)

# BFS 수행 및 결과 출력
print(bfs(graph, 1, visited))
