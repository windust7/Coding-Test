n, m = map(int, input().split())

# Please write your code here.
result = n * m

for test in range(n*m, max(n, m) - 1, -1):
    if test % n == 0 and test % m == 0:
        result = min(result, test)
print(result)