N = int(input())

# Please write your code here.
def func(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return func(N // 3) + func(N - 1)
print(func(N))