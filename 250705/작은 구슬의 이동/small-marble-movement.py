map_size, total_turn = map(int, input().split())
cur_row, cur_col, cur_dir = input().split()
cur_row, cur_col = int(cur_row), int(cur_col)
if cur_dir == "U":
    cur_dir = 0
elif cur_dir == "R":
    cur_dir = 1
elif cur_dir == "L":
    cur_dir = 2
elif cur_dir == "D":
    cur_dir = 3

def in_range(cur_row_idx, cur_col_idx):
    return cur_row_idx >= 1 and cur_row_idx <= map_size and cur_col_idx >= 1 and cur_col_idx <= map_size

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
for turn_idx in range(total_turn):
    next_row = cur_row + dx[cur_dir]
    next_col = cur_col + dy[cur_dir]
    if in_range(next_row, next_col):
        cur_row = next_row
        cur_col = next_col
    else:
        cur_dir = 3 - cur_dir
print(f"{cur_row} {cur_col}")