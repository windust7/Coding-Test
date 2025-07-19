N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
_list = []
# print(command, value)
for idx in range(len(command)):
    if command[idx] == "push":
        _list.append(value[idx])
    elif command[idx] == "size":
        print(len(_list))
    elif command[idx] == "empty":
        print(int(len(_list) == 0))
    elif command[idx] == "pop":
        print(_list.pop())
    elif command[idx] == "top":
        print(_list[-1])