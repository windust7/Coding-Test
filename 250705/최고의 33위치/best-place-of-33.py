map_size = int(input())
total_map = []
for _ in range(map_size):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)
result = 0
for row_idx in range(1, map_size-1):
    for col_idx in range(1, map_size-1):
        candidate_num = total_map[row_idx-1][col_idx-1] + total_map[row_idx-1][col_idx] + total_map[row_idx-1][col_idx+1] +\
                        total_map[row_idx][col_idx-1] + total_map[row_idx][col_idx] + total_map[row_idx][col_idx+1] +\
                        total_map[row_idx+1][col_idx-1] + total_map[row_idx+1][col_idx] + total_map[row_idx+1][col_idx+1]
        result = max(result, candidate_num)
print(result)