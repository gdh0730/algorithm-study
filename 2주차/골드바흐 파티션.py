def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n-i):
            count += 1
    print(count)