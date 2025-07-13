n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

_dict = {}

# Please write your code here.
for command in commands:
    if len(command) == 3:
        cmd, k, v = command
    else:
        cmd, k = command
    
    if cmd == "add":
        _dict[k] = v
    elif cmd == "remove":
        _dict.pop(k)
    elif cmd == "find":
        if k in _dict:
            print(_dict[k])
        else:
            print(None)