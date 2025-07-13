n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
_dict = {}

for idx, item in enumerate(arr):
    if item not in _dict:
        _dict[item] = 1
    else:
        _dict[item] += 1

for item in nums:
    if item not in _dict:
        print(0, end=" ")
    else:
        print(_dict[item], end=" ")