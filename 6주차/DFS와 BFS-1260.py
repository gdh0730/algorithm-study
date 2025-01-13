'''
**Sudo 코드**

1. **그래프 입력 처리 단계**  
   - 정점 개수 N, 간선 개수 M, 시작 정점 V를 입력받는다.  
   - M개의 간선을 입력받아 인접 리스트 graph를 생성한다.
        ex) graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]  
   - 각 정점의 인접 리스트를 **오름차순**으로 정렬하여 작은 번호부터 방문하도록 한다.

2. **DFS 탐색 단계**  
   - DFS 함수는 다음을 수행한다:
     1. 시작 정점을 방문하고 결과 리스트에 추가한다.
     2. 인접한 정점 중 방문하지 않은 정점에 대해 재귀 호출을 수행한다.

3. **BFS 탐색 단계**  
   - BFS 함수는 다음을 수행한다:
     1. 큐에 시작 정점을 추가하고 방문 처리를 한다.
     2. 큐가 빌 때까지 반복하며 현재 정점을 큐에서 꺼내고 결과 리스트에 추가한다.
     3. 인접한 정점 중 방문하지 않은 정점을 큐에 추가하고 방문 처리를 한다.

4. **출력 단계**  
   - DFS 탐색 결과와 BFS 탐색 결과를 출력한다.
'''
from collections import deque

def dfs(graph, v, visited, result):
    visited[v] = True
    result.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

def bfs(graph, v):
    queue = deque([v])
    visited = [False] * len(graph)
    visited[v] = True
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return result

# 입력 처리
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점의 인접 리스트를 오름차순으로 정렬
for adj in graph:
    adj.sort()

# DFS 수행
visited = [False] * (N + 1)
dfs_result = []
dfs(graph, V, visited, dfs_result)
print(' '.join(map(str, dfs_result)))

# BFS 수행
bfs_result = bfs(graph, V)
print(' '.join(map(str, bfs_result)))
