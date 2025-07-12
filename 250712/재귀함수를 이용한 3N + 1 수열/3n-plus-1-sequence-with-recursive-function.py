n = int(input())

# Please write your code here.
def func(n, turn):
    if n == 1:
        print(turn)
        return
    if n % 2 == 0:
        func(n // 2, turn + 1)
    else:
        func(n * 3 + 1, turn + 1)

func(n, 0)