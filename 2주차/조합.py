'''
from itertools import combinations
nums = [n for n in range(1, 101)]
com = list(combinations(nums, 6))
print(len(com))
'''
import math

n, m = map(int, input().split())
result = math.factorial(n) // (math.factorial(n-m) * math.factorial(m))
print(result)