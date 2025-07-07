map_size = int(input())
total_map = []
for _ in range(map_size):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)
cur_group = [[0] * map_size for _ in range(map_size)]

def is_possible(row_idx, col_idx):
    return 0 <= row_idx < map_size and 0 <= col_idx < map_size and cur_group[row_idx][col_idx] == 0 \
            and total_map[row_idx][col_idx] == 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def flood_fill(row_idx, col_idx, group_idx):
    cur_group[row_idx][col_idx] = group_idx
    for idx in range(4):
        next_row = row_idx + dx[idx]
        next_col = col_idx + dy[idx]
        if is_possible(next_row, next_col):
            flood_fill(next_row, next_col, group_idx)

group_list = []
group_idx = 1
for row_idx in range(map_size):
    for col_idx in range(map_size):
        if cur_group[row_idx][col_idx] == 0 and total_map[row_idx][col_idx] == 1:
            flood_fill(row_idx, col_idx, group_idx)
            cur_num = 0
            for test_row_idx in range(map_size):
                for test_col_idx in range(map_size):
                    if cur_group[test_row_idx][test_col_idx] == group_idx:
                        cur_num += 1
            group_list.append(cur_num)
            group_idx += 1

print(group_idx-1)
group_list.sort()
for item in group_list:
    print(item)