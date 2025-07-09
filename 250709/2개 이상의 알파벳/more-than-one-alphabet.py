A = input()

# Please write your code here.
result = False
for idx, test in enumerate(A):
    if idx == len(A)-1:
        continue
    else:
        if test != A[idx+1]:
            result = True
            break

if result:
    print("Yes")
else:
    print("No")