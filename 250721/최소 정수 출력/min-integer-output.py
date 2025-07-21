import heapq

num_cmd = int(input())

min_heap = []

for cmd_idx in range(num_cmd):
    cur_cmd = int(input())
    if cur_cmd == 0:
        if len(min_heap) != 0:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, cur_cmd)