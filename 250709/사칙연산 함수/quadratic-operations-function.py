a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

if o == "+":
    print(f"{a} {o} {c} = {a+c}")
elif o == "-":
    print(f"{a} {o} {c} = {a-c}")
elif o == "/":
    print(f"{a} {o} {c} = {a//c}")
elif o == "*":
    print(f"{a} {o} {c} = {a*c}")
else:
    print("False")