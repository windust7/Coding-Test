from collections import deque

map_size, num_candidate = map(int, input().split())
total_map = []
for _ in range(map_size):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)
candidate_list = []
for _ in range(num_candidate):
    row_idx, col_idx = map(int, input().split())
    candidate_list.append([row_idx-1, col_idx-1])

def bfs(row_idx, col_idx):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * map_size for _ in range(map_size)]
    queue = deque([[row_idx, col_idx]])
    visited[row_idx][col_idx] = True
    while queue:
        cur_node = queue.popleft()
        cur_row, cur_col = cur_node[0], cur_node[1]
        for idx in range(4):
            next_row = cur_row + dx[idx]
            next_col = cur_col + dy[idx]
            if next_row >= 0 and next_row < map_size and next_col >= 0 and next_col < map_size and not visited[next_row][next_col] \
                and total_map[next_row][next_col] == 0:
                visited[next_row][next_col] = True
                queue.append([next_row, next_col])
    return visited

total_visited = [[False] * map_size for _ in range(map_size)]
for candidate in candidate_list:
    cur_visited = bfs(candidate[0], candidate[1])
    for i in range(map_size):
        for j in range(map_size):
            if cur_visited[i][j]:
                total_visited[i][j] = True

result = 0
for i in range(map_size):
    for j in range(map_size):
        if total_visited[i][j]:
            result += 1
print(result)
