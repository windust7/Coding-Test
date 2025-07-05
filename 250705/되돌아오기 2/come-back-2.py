commands = list(input())
cur_row, cur_col, cur_dir = 0, 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
succeed = False
result = -1
for idx, command in enumerate(commands):
    if command == "L":
        cur_dir = (cur_dir - 1 + 4) % 4
    elif command == "R":
        cur_dir = (cur_dir + 1) % 4
    elif command == "F":
        cur_row += dx[cur_dir]
        cur_col += dy[cur_dir]
        if cur_row == 0 and cur_col == 0:
            succeed = True
            result = idx+1
            break
print(result)