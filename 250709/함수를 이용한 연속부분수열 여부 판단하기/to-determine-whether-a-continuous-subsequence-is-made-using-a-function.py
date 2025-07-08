n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def check(a, b, start_idx):
    cut_a = a[start_idx:start_idx+len(b)]
    for idx in range(len(b)):
        if cut_a[idx] != b[idx]:
            return False
    return True

result = False

if len(a) < len(b):
    print("No")
if len(a) == len(b):
    _check = True
    for idx in range(len(b)):
        if a[idx] != b[idx]:
            _check = False
    if _check:
        print("Yes")
    else:
        print("No")
else:
    _check = False
    for check_idx in range(len(a)-len(b)):
        if check(a, b, check_idx):
            _check = True
            break
    if _check:
        print("Yes")
    else:
        print("No")