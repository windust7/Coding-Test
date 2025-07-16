n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
while True:
    is_sorted = True
    for idx in range(n-1):
        if arr[idx] > arr[idx+1]:
            arr[idx+1], arr[idx] = arr[idx], arr[idx+1]
            is_sorted = False
    if is_sorted:
        break

print(" ".join(map(str, arr)))