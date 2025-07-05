map_size = int(input())

cur_num = map_size * map_size
total_map = [[0] * map_size for _ in range(map_size)]

cur_row = map_size - 1
cur_col = map_size - 1
cur_dir = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for idx in range(map_size * map_size):
    if idx == 0:
        total_map[cur_row][cur_col] = str(cur_num)
    else:
        cur_num -= 1
        next_row = cur_row + dx[cur_dir]
        next_col = cur_col + dy[cur_dir]
        if next_row >= 0 and next_row < map_size and next_col >= 0 and next_col < map_size and total_map[next_row][next_col] == 0:
            total_map[next_row][next_col] = str(cur_num)
            cur_row = next_row
            cur_col = next_col
        else:
            cur_dir = (cur_dir + 1) % 4
            cur_row += dx[cur_dir]
            cur_col += dy[cur_dir]
            total_map[cur_row][cur_col] = str(cur_num)
for row in total_map:
    print(" ".join(row))