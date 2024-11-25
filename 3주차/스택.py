N = int(input())  # 명령의 수 N을 입력받습니다.
stack = []  # 스택을 구현하기 위한 빈 리스트를 생성합니다.

for _ in range(N):
    cmd = input().strip()  # 명령을 입력받고 앞뒤 공백을 제거합니다.

    if cmd.startswith('push'):  # 명령이 'push'로 시작하는지 확인합니다.
        _, value = cmd.split()  # 'push'와 숫자를 분리합니다.
        stack.append(int(value))  # 스택에 정수를 추가합니다.

    elif cmd == 'pop':
        if stack:
            print(stack.pop())  # 스택이 비어있지 않으면 가장 위의 요소를 출력하고 제거합니다.
        else:
            print(-1)  # 스택이 비어있으면 -1을 출력합니다.

    elif cmd == 'size':
        print(len(stack))  # 스택의 크기를 출력합니다.

    elif cmd == 'empty':
        print(0 if stack else 1)  # 스택이 비어있으면 1, 아니면 0을 출력합니다.

    elif cmd == 'top':
        if stack:
            print(stack[-1])  # 스택의 가장 위에 있는 요소를 출력합니다.
        else:
            print(-1)  # 스택이 비어있으면 -1을 출력합니다.
            