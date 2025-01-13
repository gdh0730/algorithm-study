'''
Sudo 코드

1. 그래프 입력 처리 단계
- N과 M을 입력받는다.
- M개의 간선을 입력받아 무방향 그래프를 인접 리스트 graph로 생성한다.

2. DFS 탐색 함수 정의
- 현재 정점을 방문하고, 인접한 모든 정점 중 방문하지 않은 정점에 대해 재귀 호출을 수행한다.

3. 연결 요소 계산 단계
- 방문 배열 visited를 초기화한다.
- 1번 정점부터 N번 정점까지 반복하며 방문하지 않은 정점에 대해 DFS 탐색을 수행하고, 탐색이 시작될 때마다 연결 요소의 개수를 1씩 증가시킨다.

4. 출력 단계
- 최종 연결 요소의 개수를 출력한다.
'''
from sys import setrecursionlimit, stdin
setrecursionlimit(10000)  # 재귀 깊이 제한 설정
input = stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# 입력 처리
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요소 개수 계산
visited = [False] * (N + 1)
connected_components = 0

for i in range(1, N + 1):
    if not visited[i]:  # 방문하지 않은 정점에 대해 DFS 수행
        dfs(graph, i, visited)
        connected_components += 1  # 새로운 연결 요소 발견

# 출력
print(connected_components)
