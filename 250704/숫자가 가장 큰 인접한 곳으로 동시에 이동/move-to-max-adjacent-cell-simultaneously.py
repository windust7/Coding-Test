map_size, ball_num, total_turn = map(int, input().split())
total_map = []
for _ in range(map_size):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)
ball_coords = []
for _ in range(ball_num):
    cur_row, cur_col = map(int, input().split())
    ball_coords.append([cur_row - 1, cur_col - 1])

def cur_status(ball_coords):
    new_map = [[0] * map_size for _ in range(map_size)]
    for ball_coord in ball_coords:
        new_map[ball_coord[0]][ball_coord[1]] += 1
    return new_map

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for turn_idx in range(total_turn):
    cur_num_map = cur_status(ball_coords)
    for ball_idx in range(len(ball_coords)):
        cur_row = ball_coords[ball_idx][0]
        cur_col = ball_coords[ball_idx][1]
        # next_num = total_map[cur_row][cur_col]
        next_num = -int(1e9)
        changed = False
        for idx in range(4):
            next_row = cur_row + dx[idx]
            next_col = cur_col + dy[idx]
            if next_row >= 0 and next_row < map_size and next_col >= 0 and next_col < map_size:
                if next_num < total_map[next_row][next_col]:
                    next_num = total_map[next_row][next_col]
                    changed = True
                    next_row_confirm = next_row
                    next_col_confirm = next_col
        if changed:
            cur_num_map[cur_row][cur_col] -= 1
            cur_num_map[next_row_confirm][next_col_confirm] += 1
    ball_coords = []
    for row_idx in range(map_size):
        for col_idx in range(map_size):
            assert cur_num_map[row_idx][col_idx] >= 0, "ball number is below 0"
            if cur_num_map[row_idx][col_idx] == 1:
                ball_coords.append([row_idx, col_idx])

print(len(ball_coords))