a, b = map(int, input().split())

# Please write your code here.
result = 0
for test in range(a, b+1):
    if not (test % 2 == 0) and not (str(test)[-1] == "5") and not (test % 3 == 0 and test % 9 != 0):
        result += 1
        
print(result)