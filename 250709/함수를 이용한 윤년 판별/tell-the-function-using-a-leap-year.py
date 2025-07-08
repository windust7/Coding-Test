y = int(input())

# Please write your code here.
def func(num):
    if num % 4 == 0:
        if num % 100 == 0 and num % 400 != 0:
            return False
        return True
    return False
if func(y):
    print("true")
else:
    print("false")