n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str.sort()

_str = [str[idx] for idx in range(n) if t == str[idx][:len(t)]]

print(_str[k-1])