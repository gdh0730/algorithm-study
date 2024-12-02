import math

def solve():
  n = int(input())
  nums = []
  for _ in range(n):
    nums.append(int(input()))

  nums.sort()

  diffs = []
  for i in range(1, n):
    diffs.append(nums[i] - nums[i-1])

  def get_divisors(num):
    divisors = []
    for i in range(2, num + 1):
      if num % i == 0:
        divisors.append(i)
    return divisors


  g = diffs[0]
  for i in range(1, len(diffs)):
    g = math.gcd(g, diffs[i])  # math.gcd 사용


  result = get_divisors(g)
  print(*result)

solve()