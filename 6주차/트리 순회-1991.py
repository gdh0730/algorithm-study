'''
Sudo 코드

1. 그래프 입력 처리
- N을 입력받고, 각 노드와 자식 노드 정보를 입력받아 인접 리스트 형태로 트리를 저장한다.
- 자식 노드가 .으로 주어진 경우 None으로 변환하여 저장한다.

2. 순회 함수 정의
- Preorder: 현재 노드를 처리하고 왼쪽, 오른쪽 자식을 재귀 호출한다.
- Inorder: 왼쪽 자식을 먼저 재귀 호출하고 현재 노드를 처리한 후, 오른쪽 자식을 재귀 호출한다.
- Postorder: 왼쪽 자식과 오른쪽 자식을 재귀 호출한 후, 현재 노드를 처리한다.

3. 순회 수행 및 출력
- Preorder, Inorder, Postorder 순서로 순회한 결과를 출력한다.
'''
def preorder(node):
    if node is None:
        return
    result_preorder.append(node)
    preorder(tree[node][0])  # 왼쪽 자식
    preorder(tree[node][1])  # 오른쪽 자식

def inorder(node):
    if node is None:
        return
    inorder(tree[node][0])  # 왼쪽 자식
    result_inorder.append(node)
    inorder(tree[node][1])  # 오른쪽 자식

def postorder(node):
    if node is None:
        return
    postorder(tree[node][0])  # 왼쪽 자식
    postorder(tree[node][1])  # 오른쪽 자식
    result_postorder.append(node)

# 입력 처리
import sys
input = sys.stdin.readline

N = int(input().strip())  # 노드 개수
tree = {}

for _ in range(N):
    parent, left, right = input().strip().split()
    tree[parent] = (left if left != '.' else None, right if right != '.' else None)

# 순회 결과 저장 리스트
result_preorder = []
result_inorder = []
result_postorder = []

# 순회 수행
preorder('A')
inorder('A')
postorder('A')

# 결과 출력
print(''.join(result_preorder))
print(''.join(result_inorder))
print(''.join(result_postorder))
