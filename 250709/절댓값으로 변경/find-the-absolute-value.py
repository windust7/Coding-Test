n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for item in arr:
    print(f"{abs(item)}", end=" ")