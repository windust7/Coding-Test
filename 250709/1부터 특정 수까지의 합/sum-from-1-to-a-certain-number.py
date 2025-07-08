n = int(input())

# Please write your code here.
def func(n):
    result = [i for i in range(1, (n+1))]
    result_sum = sum(result)
    return result_sum / 10
print(int(func(n)))