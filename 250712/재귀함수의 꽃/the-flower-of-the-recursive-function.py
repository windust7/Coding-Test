N = int(input())

# Please write your code here.
def func(N):
    if N == 1:
        print(f"1 1", end=" ")
    else:
        print(f"{N}", end=" ")
        func(N-1)
        print(f"{N}", end=" ")

func(N)