a, b = map(int, input().split())

# Please write your code here.
def func(a, b):
    result = 0
    for test in range(a, b+1):
        str_test = str(test)
        if "3" in str_test or "6" in str_test or "9" in str_test:
            result += 1
        elif test % 3 == 0:
            result += 1
    print(result)

func(a, b)
    