n = int(input())

# Please write your code here.
def func(test):
    str_test = str(test)
    result = 0
    for i in str_test:
        result += int(i)
    if test % 2 == 0 and result % 5 ==0:
        print("Yes")
    else:
        print("No")
func(n)