map_size = int(input())
total_map = []
for _ in range(map_size):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)

def in_range(cur_row, cur_col):
    return cur_row >= 0 and cur_row < map_size and cur_col >= 0 and cur_col < map_size

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0
for row_idx in range(map_size):
    for col_idx in range(map_size):
        cur_1_num = 0
        for dir_idx in range(4):
            next_row_idx = row_idx + dx[dir_idx]
            next_col_idx = col_idx + dy[dir_idx]
            if in_range(next_row_idx, next_col_idx) and total_map[next_row_idx][next_col_idx] == 1:
                cur_1_num += 1
        if cur_1_num >= 3:
            result += 1
print(result)