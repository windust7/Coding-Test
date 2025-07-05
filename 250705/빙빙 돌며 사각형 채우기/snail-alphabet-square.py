# ord("A") == 65
# ord("Z") == 90
# chr(65) == "A"

num_row, num_col = map(int, input().split())

cur_row, cur_col = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

total_map = [[0] * num_col for _ in range(num_row)]

cur_ord = 65
cur_dir = 0

for idx in range(num_row * num_col):
    if idx == 0:
        total_map[cur_row][cur_col] = chr(cur_ord)
    else:
        cur_ord += 1
        if cur_ord == 91:
            cur_ord = 65
        next_row = cur_row + dx[cur_dir]
        next_col = cur_col + dy[cur_dir]
        if next_row >= 0 and next_row < num_row and next_col >= 0 and next_col < num_col and total_map[next_row][next_col] == 0:
            total_map[next_row][next_col] = chr(cur_ord)
            cur_row = next_row
            cur_col = next_col
        else:
            cur_dir = (cur_dir + 1) % 4
            cur_row += dx[cur_dir]
            cur_col += dy[cur_dir]
            total_map[cur_row][cur_col] = chr(cur_ord)
for row in total_map:
    print(" ".join(row))