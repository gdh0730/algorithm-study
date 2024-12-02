N = int(input())  # 테스트 데이터의 수를 입력받습니다.

for _ in range(N):
    ps = input().strip()  # 괄호 문자열을 입력받습니다.
    stack = []  # 스택을 초기화합니다.
    is_vps = True  # VPS 여부를 나타내는 변수를 초기화합니다.

    for char in ps:
        if char == '(':  # 여는 괄호인 경우
            stack.append(char)  # 스택에 추가합니다.
        elif char == ')':  # 닫는 괄호인 경우
            if stack:
                stack.pop()  # 스택에서 여는 괄호를 제거합니다.
            else:
                is_vps = False  # 스택이 비어있으면 VPS가 아닙니다.
                break  # 더 이상 검사할 필요가 없습니다.

    if stack:  # 모든 문자를 검사한 후 스택이 비어있지 않으면
        is_vps = False  # VPS가 아닙니다.

    print('YES' if is_vps else 'NO')  # 결과를 출력합니다.
    