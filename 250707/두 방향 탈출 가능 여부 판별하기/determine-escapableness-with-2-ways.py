num_row, num_col = map(int, input().split())
total_map = []
for _ in range(num_row):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)

cur_row, cur_col = 0, 0
visited = [[False] * num_col for _ in range(num_row)]

def possible_state(row_idx, col_idx):
    return 0 <= row_idx < num_row and 0 <= col_idx < num_col and not visited[row_idx][col_idx] and total_map[row_idx][col_idx] == 1

dx = [1, 0]
dy = [0, 1]

def dfs(row_idx, col_idx):
    # for row in visited:
    #     print(row)
    # print()
    visited[row_idx][col_idx] = True
    for idx in range(2):
        if possible_state(row_idx+dx[idx], col_idx+dy[idx]):
            dfs(row_idx+dx[idx], col_idx+dy[idx])

dfs(cur_row, cur_col)

print(int(visited[num_row-1][num_col-1]))