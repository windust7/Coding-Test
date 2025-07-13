n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
_dict = {}

for idx, word in enumerate(words[1:]):
    _dict[word] = idx+1

for query in queries:
    if query.isalpha():
        print(_dict[query])
    else:
        print(words[int(query)])