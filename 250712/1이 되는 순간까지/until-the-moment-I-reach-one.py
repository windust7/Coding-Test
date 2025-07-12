N = int(input())

# Please write your code here.
def func(N, turn):
    if N == 1:
        print(turn)
        return
    if N % 2 == 0:
        func(N // 2, turn + 1)
    else:
        func(N // 3, turn + 1)

func(N, 0)