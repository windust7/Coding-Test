n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    min_i = i
    for j in range(i, n):
        if arr[j] < arr[min_i]:
            min_i = j
    arr[i], arr[min_i] = arr[min_i], arr[i]
print(" ".join(map(str, arr)))