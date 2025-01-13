'''
Sudo 코드

1. 입력 처리 단계
- 테스트 케이스 수 T를 입력받는다.
- 각 테스트 케이스에 대해 다음을 수행:
    1. 순열의 크기 N을 입력받는다.
    2. 순열을 리스트로 입력받는다.

2. DFS 탐색 함수 정의
- 입력: 시작 정점 v, 방문 배열 visited
- 현재 정점을 방문 처리하고, 다음 정점으로 이동하여 재귀적으로 호출한다.

3. 사이클 계산 단계
- 방문 배열 visited를 초기화한다.
- 각 정점에 대해 방문하지 않았다면, DFS를 수행하고 사이클 개수를 1 증가시킨다.

4. 출력 단계
- 각 테스트 케이스에 대해 구한 사이클 개수를 출력한다.
'''
def dfs(v, graph, visited):
    visited[v] = True
    next_node = graph[v]
    if not visited[next_node]:
        dfs(next_node, graph, visited)

def count_cycles(N, permutation):
    # 1-based index로 그래프 구성 (순열 원소는 1부터 시작)
    graph = [0] + permutation
    visited = [False] * (N + 1)
    cycle_count = 0

    for i in range(1, N + 1):
        if not visited[i]:  # 방문하지 않은 정점에서 DFS 시작
            dfs(i, graph, visited)
            cycle_count += 1  # 새로운 사이클 발견

    return cycle_count

# 입력 처리
T = int(input())
for _ in range(T):
    N = int(input())
    permutation = list(map(int, input().split()))
    print(count_cycles(N, permutation))
