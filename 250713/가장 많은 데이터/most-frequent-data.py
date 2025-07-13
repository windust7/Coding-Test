n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
_dict = {}
for idx, item in enumerate(words):
    if item in _dict:
        _dict[item] += 1
    else:
        _dict[item] = 1
max_item = -int(1e9)
for key in _dict.keys():
    max_item = max(_dict[key], max_item)
print(max_item)