from collections import deque

num_row, num_col = map(int, input().split())
total_map = []
for _ in range(num_row):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)

cur_row = 0
cur_col = 0
visited = [[False] * num_col for _ in range(num_row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(row_idx, col_idx):
    result = 0
    queue = deque([[row_idx, col_idx]])
    visited[row_idx][col_idx] = True
    while queue:
        cur_node = queue.popleft()
        cur_row_idx, cur_col_idx = cur_node[0], cur_node[1]
        for idx in range(4):
            next_row_idx = cur_row_idx + dx[idx]
            next_col_idx = cur_col_idx + dy[idx]
            if next_row_idx >= 0 and next_row_idx < num_row and next_col_idx >= 0 and next_col_idx < num_col and \
                not visited[next_row_idx][next_col_idx] and total_map[next_row_idx][next_col_idx] == 1:
                visited[next_row_idx][next_col_idx] = True
                if next_row_idx == (num_row - 1) and next_col_idx == (num_col - 1):
                    result = 1
                else:
                    queue.append([next_row_idx, next_col_idx])
    return result


print(bfs(cur_row, cur_col))