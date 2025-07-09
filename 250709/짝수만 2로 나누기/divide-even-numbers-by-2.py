n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def func(arr):
    for idx, item in enumerate(arr):
        if item % 2 == 0:
            arr[idx] = item // 2

func(arr)
print(" ".join(map(str, arr)))