from math import sqrt, isqrt, ceil

n = int(input())
nums = list(map(int, input().split()))

max_num = max(nums)
limit = isqrt(max_num) + 1
isprime = [True] * (limit + 1)
isprime[0] = isprime[1] = False
for i in range(2, limit + 1):
    if isprime[i]:
        for j in range(i * i, limit + 1, i):
            isprime[j] = False

primes = {i * i for i in range(2, limit + 1) if isprime[i]}

def istprime(n):
    return n in primes

for num in nums:
    if istprime(num):
        print("YES")
    else:
        print("NO")
