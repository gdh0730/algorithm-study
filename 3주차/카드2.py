from collections import deque

N = int(input())
queue = deque(range(1, N+1))  # 1부터 N까지의 숫자를 큐에 저장

while len(queue) > 1:
    queue.popleft()          # 제일 위에 있는 카드를 버림
    queue.append(queue.popleft())  # 다음 카드를 제일 아래로 옮김

print(queue[0])  # 마지막에 남은 카드 출력
