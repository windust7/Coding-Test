n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for sorted_idx in range(n-1):
    start_idx = sorted_idx + 1
    while sorted_idx >= 0 and arr[start_idx] < arr[sorted_idx]:
        arr[start_idx], arr[sorted_idx] = arr[sorted_idx], arr[start_idx]
        start_idx -= 1
        sorted_idx -= 1
print(" ".join(map(str, arr)))