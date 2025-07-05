map_size = int(input())
total_map = []
for _ in range(map_size):
    cur_row = list(input())
    total_map.append(cur_row)
start_num = int(input())

first_dx = [-1, 1, 0, 0]    # /
first_dy = [0, 0, -1, 1]    # /

second_dx = [-1, 1, 0, 0]   # \
second_dy = [0, 0, 1, -1]   # \

first_to_second = {0: 0, 1: 1, 2: 3, 3: 2}
second_to_first = {0: 0, 1: 1, 2: 3, 3: 2}

which_side = (start_num-1) // map_size
if which_side == 0:
    cur_row = 0
    cur_col = start_num - 1
    cur_first_dir = 1
    cur_second_dir = 1
elif which_side == 1:
    cur_col = map_size - 1
    cur_row = start_num - map_size
    cur_first_dir = 3
    cur_second_dir = 2
elif which_side == 2:
    cur_row = start_num - 1
    cur_col = map_size * 3 - start_num
    cur_first_dir = 0
    cur_second_dir = 0
elif which_side == 3:
    cur_col = 0
    cur_row = map_size * 4 - start_num
    cur_first_dir = 2
    cur_second_dir = 3

result = 0
first = True
while cur_row >= 0 and cur_row < map_size and cur_col >= 0 and cur_col < map_size:
    # print(f"{cur_row}, {cur_col}")
    result += 1
    if result == 1:
        cur_dir = cur_first_dir
    if total_map[cur_row][cur_col] == "/":
        dx = first_dx
        dy = first_dy
        if not first:
            cur_dir = second_to_first[cur_dir]
        first = True
        cur_dir = 3 - cur_dir
        cur_row += dx[cur_dir]
        cur_col += dy[cur_dir]
    elif total_map[cur_row][cur_col] == "\\":
        dx = second_dx
        dy = second_dy
        if first:
            cur_dir = first_to_second[cur_dir]
        first = False
        cur_dir = 3 - cur_dir
        cur_row += dx[cur_dir]
        cur_col += dy[cur_dir]
print(result)