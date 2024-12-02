N = int(input())
num = []

for _ in range(N):
    n = int(input())
    num.append(n)

# 버블 정렬 알고리즘을 사용하여 리스트를 정렬합니다.
for i in range(N - 1):
    for j in range(N - 1 - i):
        if num[j] > num[j + 1]:
            # 두 요소를 교환합니다.
            num[j], num[j + 1] = num[j + 1], num[j]

for n in num:
    print(n)
