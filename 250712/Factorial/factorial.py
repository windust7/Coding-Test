N = int(input())

# Please write your code here.
def func(N):
    if N == 0 or N == 1:
        return 1
    return func(N-1) * N

print(func(N))