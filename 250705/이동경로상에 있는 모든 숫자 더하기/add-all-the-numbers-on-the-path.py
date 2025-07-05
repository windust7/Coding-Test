map_size, total_turn = map(int, input().split())
commands = list(input())
total_map = []
for _ in range(map_size):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)

cur_row = (map_size - 1) // 2
cur_col = (map_size - 1) // 2
cur_dir = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = total_map[cur_row][cur_col]
for command in commands:
    if command == "L":
        cur_dir = (cur_dir - 1 + 4) % 4
    elif command == "R":
        cur_dir = (cur_dir + 1) % 4
    elif command == "F":
        next_row = cur_row + dx[cur_dir]
        next_col = cur_col + dy[cur_dir]
        if next_row >= 0 and next_row < map_size and next_col >= 0 and next_col < map_size:
            result += total_map[next_row][next_col]
            cur_row = next_row
            cur_col = next_col

print(result)