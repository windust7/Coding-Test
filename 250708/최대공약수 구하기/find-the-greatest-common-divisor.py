n, m = map(int, input().split())

# Please write your code here. 
gcd = 1
for test in range(1, min(n, m)+1):
    if n % test == 0 and m % test == 0:
        gcd = test
print(gcd)