map_size = int(input())
total_map = []
for _ in range(map_size):
    cur_row = list(input())
    total_map.append(cur_row)
start_num = int(input())

first_dx = [-1, 1, 0, 0]    # /, 북 남 서 동
first_dy = [0, 0, -1, 1]    # /

second_dx = [-1, 1, 0, 0]   # \, 북 남 동 서
second_dy = [0, 0, 1, -1]   # \

first_to_second = {0: 0, 1: 1, 2: 3, 3: 2}
second_to_first = {0: 0, 1: 1, 2: 3, 3: 2}

if 1 <= start_num <= map_size:
    cur_row = 0
    cur_col = start_num - 1
    cur_dir = 1
elif (map_size + 1) <= start_num <= (2 * map_size):
    cur_col = map_size - 1
    cur_row = start_num - map_size
    cur_dir = 2
elif (2 * map_size + 1) <= start_num <= (3 * map_size):
    cur_row = start_num - 1
    cur_col = map_size * 3 - start_num
    cur_dir = 0
elif (3 * map_size + 1) <= start_num <= (4 * map_size):
    cur_col = 0
    cur_row = map_size * 4 - start_num
    cur_dir = 3

result = 0
first = True
while cur_row >= 0 and cur_row < map_size and cur_col >= 0 and cur_col < map_size:
    # print(f"{cur_row}, {cur_col}")
    result += 1
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