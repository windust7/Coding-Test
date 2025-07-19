n = int(input())

# Please write your code here.
from collections import deque
queue = deque([idx for idx in range(n)])

idx = 0
while len(queue) != 1:
    queue.popleft()
    move_num = queue.popleft()
    queue.append(move_num)
print(queue[0] + 1)