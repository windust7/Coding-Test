import heapq

num_point, num_cmd = map(int, input().split())

_list = []
for _ in range(num_point):
    cur_point = list(map(lambda x: int(x), input().split()))
    input_tuple = tuple([cur_point[0] + cur_point[1]] + cur_point)
    heapq.heappush(_list, input_tuple)

for cmd_idx in range(num_cmd):
    cur_point = heapq.heappop(_list)
    new_x, new_y = cur_point[1] + 2, cur_point[2] + 2
    heapq.heappush(_list, (new_x + new_y, new_x, new_y))

result = heapq.heappop(_list)
print(f"{result[1]} {result[2]}")