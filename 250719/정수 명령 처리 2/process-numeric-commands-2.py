N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
from collections import deque
queue = deque([])
for idx in range(len(command)):
    if command[idx] == "push":
        queue.append(A[idx])
    elif command[idx] == "pop":
        print(queue.popleft())
    elif command[idx] == "size":
        print(len(queue))
    elif command[idx] == "empty":
        print(int(len(queue) == 0))
    elif command[idx] == "front":
        print(queue[0])
    else:
        print(f"Wrong cmd: {command[idx]}")