import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        else:
            return -heapq.heappop(self.items)
    
    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        else:
            return -self.items[0]

num_cmd = int(input())

max_heap = PriorityQueue()

for cmd_idx in range(num_cmd):
    cur_cmd = input()
    if not cur_cmd[-1].isalpha():
        cur_cmd, cur_num = tuple(cur_cmd.split())
        cur_num = int(cur_num)
        max_heap.push(cur_num)
    else:
        if cur_cmd == "pop":
            print(max_heap.pop())
        elif cur_cmd == "size":
            print(max_heap.size())
        elif cur_cmd == "empty":
            print(int(max_heap.empty()))
        elif cur_cmd == "top":
            print(max_heap.top())
