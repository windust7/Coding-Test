a, b = map(int, input().split())

# Please write your code here.
def is_prime(num):
    for test in range(2, num):
        if num % test == 0:
            return False
    return True

def func(a, b):
    result = 0
    for test in range(a, b+1):
        if is_prime(test):
            result += test
    print(result)

func(a, b)