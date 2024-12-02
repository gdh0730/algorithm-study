import sys

# 입력의 수가 많으므로 sys.stdin.readline()을 사용하여 빠르게 입력받습니다.
N = int(sys.stdin.readline())
members = []

# 각 회원의 나이, 이름, 가입 순서를 저장합니다.
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    members.append((age, i, name))  # 가입 순서를 저장하기 위해 인덱스 i를 함께 저장합니다.

# 나이순으로 정렬합니다.
# 파이썬의 정렬은 안정 정렬이므로, 나이가 같은 경우 가입 순서가 유지됩니다.
members.sort(key=lambda x: x[0])

# 정렬된 회원 정보를 출력합니다.
for member in members:
    print(f"{member[0]} {member[2]}")
