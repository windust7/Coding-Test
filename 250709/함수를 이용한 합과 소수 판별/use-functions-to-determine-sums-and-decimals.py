a, b = map(int, input().split())

# Please write your code here.
def is_prime(num):
    for test in range(2, num):
        if num % test == 0:
            return False
    return True

def check_2(num):
    str_num = str(num)
    result = 0
    for i in str_num:
        result += int(i)
    return (result % 2 == 0)

result = 0
for test in range(a, b+1):
    if is_prime(test) and check_2(test):
        result += 1
print(result)