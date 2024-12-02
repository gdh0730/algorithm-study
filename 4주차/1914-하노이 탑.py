def hanoi(n, start, target, auxiliary, moves):
    if n == 1:
        # 원판 1개를 단순히 start -> target으로 이동
        moves.append((start, target))
        return
    # N-1개의 원판을 start에서 auxiliary로 옮김
    hanoi(n - 1, start, auxiliary, target, moves)
    # 가장 큰 원판을 start에서 target으로 옮김
    moves.append((start, target))
    # N-1개의 원판을 auxiliary에서 target으로 옮김
    hanoi(n - 1, auxiliary, target, start, moves)

# 입력 처리
N = int(input())

# 이동 순서를 저장할 리스트
moves = []

# 하노이 탑 이동 수행
hanoi(N, 1, 3, 2, moves)

# 최소 이동 횟수는 2^N - 1
print(len(moves))

# N이 20 이하인 경우에만 이동 순서를 출력
if N <= 20:
    for move in moves:
        print(move[0], move[1])
