N = int(input())

# Please write your code here.
def func(N):
    if 0 <= N <= 9:
        return N ** 2
    return func(N // 10) + (N % 10) ** 2

print(func(N))