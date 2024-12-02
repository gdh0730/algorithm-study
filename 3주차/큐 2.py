from collections import deque

N = int(input())  # 명령의 수를 입력받습니다.
queue = deque()  # 큐를 초기화합니다.

for _ in range(N):
    cmd = input().strip()  # 명령을 입력받고 양쪽 공백을 제거합니다.

    if cmd.startswith('push'):
        _, value = cmd.split()
        queue.append(int(value))  # 큐의 뒤에 요소를 추가합니다.
    elif cmd == 'pop':
        if queue:
            print(queue.popleft())  # 큐의 앞에서 요소를 제거하고 출력합니다.
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))  # 큐의 크기를 출력합니다.
    elif cmd == 'empty':
        print(0 if queue else 1)  # 큐가 비어있는지 여부를 출력합니다.
    elif cmd == 'front':
        if queue:
            print(queue[0])  # 큐의 가장 앞에 있는 요소를 출력합니다.
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[-1])  # 큐의 가장 뒤에 있는 요소를 출력합니다.
        else:
            print(-1)
            