n = int(input())
arr = list(map(int, input().split()))

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr[0]
    else:
        return lcm(arr[n - 1], lcm_recursive(arr, n - 1))

print(lcm_recursive(arr))