total_turn = int(input())
commands = []
dir_dict = {"N": 0, "E": 1, "S": 2, "W": 3}
for idx in range(total_turn):
    direction, length = input().split()
    direction = dir_dict[direction]
    length = int(length)
    commands.append((direction, length))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cur_row, cur_col = 0, 0

cur_timestep = 0
succeed = False
for command_idx in range(total_turn):
    cur_dir, cur_length = commands[command_idx]
    for timestep in range(cur_length):
        cur_row += dx[cur_dir]
        cur_col += dy[cur_dir]
        cur_timestep += 1
        if cur_row == 0 and cur_col == 0:
            succeed = True
            break
    if succeed:
        break
if succeed:
    print(cur_timestep)
else:
    print(-1)