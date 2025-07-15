from collections import deque

map_size, rotten_num = map(int, input().split())
total_map = []
start_list = []
rotten_list = []
for row_idx in range(map_size):
    cur_row = list(map(int, input().split()))
    for col_idx in range(map_size):
        if cur_row[col_idx] == 1:
            start_list.append([row_idx, col_idx])
        elif cur_row[col_idx] == 2:
            rotten_list.append([row_idx, col_idx])
    total_map.append(cur_row)

result = [[-1] * map_size for _ in range(map_size)]
for rotten in rotten_list:
    rotten_row, rotten_col = rotten[0], rotten[1]
    result[rotten_row][rotten_col] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for start_idx, start in enumerate(start_list):
    visited = [[0] * map_size for _ in range(map_size)]
    cur_row, cur_col = start[0], start[1]
    queue = deque([[cur_row, cur_col]])
    found = False
    while queue:
        cur_node = queue.popleft()
        cur_row, cur_col = cur_node[0], cur_node[1]
        for idx in range(4):
            next_row = cur_row + dx[idx]
            next_col = cur_col + dy[idx]
            if 0 <= next_row < map_size and 0 <= next_col < map_size and visited[next_row][next_col] == 0 and not ((next_row, next_col) == (start[0], start[1])) and total_map[next_row][next_col] != 0:
                visited[next_row][next_col] = visited[cur_row][cur_col] + 1
                if total_map[next_row][next_col] == 2:
                    result[start[0]][start[1]] = visited[next_row][next_col]
                    found = True
                else:
                    queue.append([next_row, next_col])
        if found:
            break
    if not found:
        result[start[0]][start[1]] = -2

for row in result:
    print(" ".join(map(str, row)))