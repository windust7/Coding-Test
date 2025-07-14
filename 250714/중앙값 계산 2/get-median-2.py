n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for idx in range(n):
    if idx % 2 == 0:
        if idx != len(arr) - 1:
            current_arr = sorted(arr[:idx+1])
        else:
            current_arr = sorted(arr)
        print(current_arr[idx // 2], end=" ")