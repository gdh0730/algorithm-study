from collections import deque

N, K = map(int, input().split())  # N과 K를 입력받습니다.

queue = deque(range(1, N+1))  # 1부터 N까지의 숫자를 덱에 저장합니다.
result = []  # 제거된 사람들을 순서대로 저장할 리스트입니다.

while queue:
    queue.rotate(-(K-1))  # K-1만큼 회전시켜서 K번째 사람이 앞에 오도록 합니다.
    result.append(queue.popleft())  # 앞의 사람을 제거하고 결과에 추가합니다.

# 결과를 형식에 맞게 출력합니다.
print("<" + ", ".join(map(str, result)) + ">")
