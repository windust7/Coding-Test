map_size, total_turn = map(int, input().split())

total_map = [[False] * map_size for _ in range(map_size)]

commands = []
for _ in range(total_turn):
    cur_row, cur_col = map(int, input().split())
    commands.append((cur_row-1, cur_col-1))

def check_comfortable(row_idx, col_idx):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    colored_num = 0
    for idx in range(4):
        next_row = row_idx + dx[idx]
        next_col = col_idx + dy[idx]
        if next_row >= 0 and next_row < map_size and next_col >= 0 and next_col < map_size and total_map[next_row][next_col]:
            colored_num += 1
    return (colored_num == 3)

for command in commands:
    cur_row, cur_col = command
    total_map[cur_row][cur_col] = True
    if check_comfortable(cur_row, cur_col):
        print(1)
    else:
        print(0)