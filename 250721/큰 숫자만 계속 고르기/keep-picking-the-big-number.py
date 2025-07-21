import heapq

num_number, num_cmd = map(int, input().split())

number_list = list(map(lambda x: -int(x), input().split()))

number_list.sort()

class PriorityQueue:
    def __init__(self, _list):
        self._list = _list
    
    def pop(self):
        return -heapq.heappop(self._list)
    
    def top(self):
        return -self._list[0]

    def push(self, data):
        heapq.heappush(self._list, -data)

max_heap = PriorityQueue(number_list)
for cmd_idx in range(num_cmd):
    cur_max = max_heap.pop()
    max_heap.push(cur_max-1)

print(max_heap.top())