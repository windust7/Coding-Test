num_row, num_col, total_wind = map(int, input().split())
total_map = []
for _ in range(num_row):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)
wind_list = []
for _ in range(total_wind):
    start_row, start_col, end_row, end_col = map(int, input().split())
    wind_list.append([start_row - 1, start_col - 1, end_row - 1, end_col - 1])


def wind_phase_1(start_row_idx, start_col_idx, end_row_idx, end_col_idx):
    tmp = [[0] * (end_col_idx - start_col_idx + 1) for _ in range(end_row_idx - start_row_idx + 1)]
    for row_idx in range((end_row_idx - start_row_idx) + 1):
        for col_idx in range((end_col_idx - start_col_idx) + 1):
            tmp[row_idx][col_idx] = total_map[row_idx + start_row_idx][col_idx + start_col_idx]
    for row_idx in range((end_row_idx - start_row_idx)):
        total_map[start_row_idx + row_idx][start_col_idx] = tmp[row_idx+1][0]
        total_map[start_row_idx + row_idx + 1][end_col_idx] = tmp[row_idx][(end_col_idx - start_col_idx)]
    for col_idx in range((end_col_idx - start_col_idx)):
        total_map[start_row_idx][start_col_idx + col_idx + 1] = tmp[0][col_idx]
        total_map[end_row_idx][start_col_idx + col_idx] = tmp[(end_row_idx - start_row_idx)][col_idx + 1]


def wind_phase_2(start_row_idx, start_col_idx, end_row_idx, end_col_idx):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    tmp = [[0] * (end_col_idx - start_col_idx + 1) for _ in range(end_row_idx - start_row_idx + 1)]
    for row_idx in range(start_row_idx, (end_row_idx + 1)):
        for col_idx in range(start_col_idx, (end_col_idx + 1)):
            total_sum = total_map[row_idx][col_idx]
            total_num = 1
            for idx in range(4):
                next_row = row_idx + dx[idx]
                next_col = col_idx + dy[idx]
                if next_row >= 0 and next_row < num_row and next_col >= 0 and next_col < num_col:
                    total_sum += total_map[next_row][next_col]
                    total_num += 1
            tmp[row_idx - start_row_idx][col_idx - start_col_idx] = total_sum // total_num
    for row_idx in range(start_row_idx, (end_row_idx + 1)):
        for col_idx in range(start_col_idx, (end_col_idx + 1)):
            total_map[row_idx][col_idx] = tmp[row_idx - start_row_idx][col_idx - start_col_idx]


for wind in wind_list:

    start_r, start_c, end_r, end_c = wind[0], wind[1], wind[2], wind[3]
    wind_phase_1(start_r, start_c, end_r, end_c)
    wind_phase_2(start_r, start_c, end_r, end_c)


for row in total_map:
    for item in row:
        print(item, end=" ")
    print()
