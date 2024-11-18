import math

n = int(input())
a_nums = list(map(int, input().split()))
m = int(input())
b_nums = list(map(int, input().split()))

a = math.prod(a_nums)
b = math.prod(b_nums)

result = math.gcd(a, b)

print(str(result)[-9:].zfill(9))