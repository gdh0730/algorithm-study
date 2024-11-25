from collections import deque

N = int(input())  # 명령의 수를 입력받습니다.
deque = deque()  # 덱을 초기화합니다.

for _ in range(N):
    cmd = input().strip()  # 명령을 입력받고 양쪽 공백을 제거합니다.

    if cmd.startswith('push_front'):
        _, X = cmd.split()
        deque.appendleft(int(X))  # 덱의 앞에 요소를 추가합니다.
    elif cmd.startswith('push_back'):
        _, X = cmd.split()
        deque.append(int(X))  # 덱의 뒤에 요소를 추가합니다.
    elif cmd == 'pop_front':
        if deque:
            print(deque.popleft())  # 덱의 가장 앞의 요소를 제거하고 출력합니다.
        else:
            print(-1)  # 덱이 비어있으면 -1을 출력합니다.
    elif cmd == 'pop_back':
        if deque:
            print(deque.pop())  # 덱의 가장 뒤의 요소를 제거하고 출력합니다.
        else:
            print(-1)
    elif cmd == 'size':
        print(len(deque))  # 덱에 들어있는 정수의 개수를 출력합니다.
    elif cmd == 'empty':
        print(0 if deque else 1)  # 덱이 비어있으면 1, 아니면 0을 출력합니다.
    elif cmd == 'front':
        if deque:
            print(deque[0])  # 덱의 가장 앞에 있는 요소를 출력합니다.
        else:
            print(-1)
    elif cmd == 'back':
        if deque:
            print(deque[-1])  # 덱의 가장 뒤에 있는 요소를 출력합니다.
        else:
            print(-1)
            