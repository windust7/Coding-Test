total_row, total_col = map(int, input().split())
total_map = [[0] * total_col for _ in range(total_row)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cur_row = 0
cur_col = 0
cur_dir = 0

for idx in range(total_row * total_col):
    if idx == 0:
        total_map[cur_row][cur_col] = str(idx + 1)
    else:
        next_row = cur_row + dx[cur_dir]
        next_col = cur_col + dy[cur_dir]
        if next_row >= 0 and next_row < total_row and next_col >= 0 and next_col < total_col and total_map[next_row][next_col] == 0:
            total_map[next_row][next_col] = str(idx + 1)
            cur_row = next_row
            cur_col = next_col
        else:
            cur_dir = (cur_dir + 1) % 4
            cur_row += dx[cur_dir]
            cur_col += dy[cur_dir]
            total_map[cur_row][cur_col] = str(idx + 1)

for row in total_map:
    print(" ".join(row))