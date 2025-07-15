from collections import deque

row_num, col_num = map(int, input().split())
total_map = []
for row_idx in range(row_num):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)

visited = [[0] * col_num for _ in range(row_num)]

cur_row, cur_col = 0, 0

queue = deque([[cur_row, cur_col]])
visited[cur_row][cur_col] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    cur_node = queue.popleft()
    cur_row, cur_col = cur_node[0], cur_node[1]
    for idx in range(4):
        next_row = cur_row + dx[idx]
        next_col = cur_col + dy[idx]
        if 0 <= next_row < row_num and 0 <= next_col < col_num and visited[next_row][next_col] == 0 and total_map[next_row][next_col] == 1 and not (next_row == 0 and next_col == 0):
            visited[next_row][next_col] = visited[cur_row][cur_col] + 1
            queue.append([next_row, next_col])
print(visited[row_num-1][col_num-1])