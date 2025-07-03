n, row_idx, col_idx = map(int, input().split())
row_idx -= 1
col_idx -= 1
total_map = []
for _ in range(n):
    total_map.append(list(map(int, input().split())))

finish = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(total_map[row_idx][col_idx], end=" ")
while not finish:
    changed = False
    for idx in range(4):
        next_x = row_idx + dx[idx]
        next_y = col_idx + dy[idx]
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
            if total_map[row_idx][col_idx] < total_map[next_x][next_y]:
                row_idx = next_x
                col_idx = next_y
                print(total_map[row_idx][col_idx], end=" ")
                changed = True
                break
    if not changed:
        finish = True