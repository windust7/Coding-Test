n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
from collections import deque

queue = deque([])

for idx in range(len(cmd)):
    if cmd[idx] == 'push_front':
        queue.appendleft(num[idx])
    elif cmd[idx] == "push_back":
        queue.append(num[idx])
    elif cmd[idx] == "pop_front":
        print(queue.popleft())
    elif cmd[idx] == "pop_back":
        print(queue.pop())
    elif cmd[idx] == "size":
        print(len(queue))
    elif cmd[idx] == "empty":
        print(int(len(queue)== 0))
    elif cmd[idx] == "front":
        print(queue[0])
    elif cmd[idx] == "back":
        print(queue[-1])