K = int(input())  # 입력받을 숫자의 개수 K를 입력받습니다.
stack = []  # 숫자를 저장할 스택을 초기화합니다.

for _ in range(K):
    num = int(input())  # 숫자를 입력받습니다.
    if num == 0:
        if stack:
            stack.pop()  # 0이면 가장 최근에 추가된 숫자를 제거합니다.
    else:
        stack.append(num)  # 0이 아니면 스택에 숫자를 추가합니다.

print(sum(stack))  # 스택에 남은 숫자들의 합을 출력합니다.
