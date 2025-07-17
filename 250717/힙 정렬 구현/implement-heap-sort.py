n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
print(" ".join(map(str, sorted(arr))))