'''
Sudo 코드

1. 그래프 입력 처리
- 노드 수 N을 입력받고, N-1개의 간선을 입력받아 인접 리스트 형태로 그래프를 생성한다.

2. BFS 또는 DFS 탐색 단계
- 루트 노드(1번)부터 탐색을 시작하여 연결된 모든 노드에 대해 부모를 기록합니다.
- 방문 배열을 사용하여 방문 여부를 체크하며, 이미 방문한 노드는 탐색하지 않습니다.

3. 출력 단계
- 2번 노드부터 N번 노드까지의 부모를 순서대로 출력합니다.
'''
import sys
from collections import deque

input = sys.stdin.readline

def find_parents(N, graph):
    parent = [0] * (N + 1)  # 부모를 저장할 배열
    visited = [False] * (N + 1)
    
    queue = deque([1])  # BFS를 위한 큐 초기화 (루트 노드는 1)
    visited[1] = True
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                parent[neighbor] = current  # 부모 기록
                visited[neighbor] = True
                queue.append(neighbor)
    
    return parent

# 입력 처리
N = int(input().strip())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

# 부모 찾기 수행
parent = find_parents(N, graph)

# 결과 출력 (2번 노드부터 N번 노드까지)
for i in range(2, N + 1):
    print(parent[i])
