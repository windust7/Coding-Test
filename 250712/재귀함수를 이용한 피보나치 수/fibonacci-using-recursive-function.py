N = int(input())

# Please write your code here.
def func(N):
    if N == 1 or N == 2:
        return 1
    return func(N-1) + func(N-2)

print(func(N))