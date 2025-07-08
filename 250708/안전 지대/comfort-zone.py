from collections import deque

num_row, num_col = map(int, input().split())
total_map = []
max_num = 0
for _ in range(num_row):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)
    max_num = max(max_num, max(cur_row))

max_region = -int(1e9)
max_rain = None

def cal_possible_region(rain):
    result_region = [[False] * num_col for _ in range(num_row)]
    for row_idx in range(num_row):
        for col_idx in range(num_col):
            result_region[row_idx][col_idx] = (total_map[row_idx][col_idx] > rain)
    return result_region

def cal_region(poss_region):
    group_idx = 0
    tmp = [[0] * num_col for _ in range(num_row)]
    for row_idx in range(num_row):
        for col_idx in range(num_col):
            if poss_region[row_idx][col_idx] and tmp[row_idx][col_idx] == 0:
                group_idx += 1
                tmp = bfs(row_idx, col_idx, tmp, group_idx, poss_region)
    return group_idx

def bfs(row_idx, col_idx, tmp, group_idx, poss_region):
    queue = deque([[row_idx, col_idx]])
    tmp[row_idx][col_idx] = group_idx
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        cur_node = queue.popleft()
        cur_row, cur_col = cur_node[0], cur_node[1]
        for idx in range(4):
            next_row = cur_row + dx[idx]
            next_col = cur_col + dy[idx]
            if 0 <= next_row < num_row and 0 <= next_col < num_col and poss_region[next_row][next_col] and \
                tmp[next_row][next_col] == 0:
                tmp[next_row][next_col] = group_idx
                queue.append([next_row, next_col])
    return tmp

for cur_rain in range(1, (max_num+1)):
    possible_region = cal_possible_region(cur_rain)
    cur_region = cal_region(possible_region)
    if cur_region > max_region:
        max_rain = cur_rain
        max_region = cur_region
print(f"{max_rain} {max_region}")