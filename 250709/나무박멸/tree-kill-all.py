"""
n x n 
제초제: 
k의 범위만큼 대각선, 벽에 막힘
각 칸중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제
c년만큼 유지하고 사라짐. 다시 뿌리면 다시 c년동안
가장 많이 제초 가능한 곳으로!

나무: 
인접한 4개의 칸 중 나무가 있는 칸의 수만큼 성장, 모든 나무가 동시에 성장
기존에 있던 나무는 인접한 4개의 칸 중에 아무것도 없는 칸에 번식 (각 칸의 나무 그루 수 // 총 번식이 가능한 칸의 개수)만큼

1. 나무 성장
2. 나무 번식
3. 제초제 뿌리기
4. 시간 지난 제초제 해제

"""

map_size, total_turn, kill_range, kill_remain = map(int, input().split())

INF = int(1e9)

total_map = []
for row_idx in range(map_size):
    cur_row = list(map(int, input().split()))
    if -1 in cur_row:
        for col_idx in range(map_size):
            if cur_row[col_idx] == -1:
                cur_row[col_idx] = -INF
    total_map.append(cur_row)

def visualize():
    for row in total_map:
        for item in row:
            if item == -INF:
                print("X", end="")
            else:
                print(item, end= "")
            print("\t", end="")
        print()
    print()

def in_range(row_idx, col_idx):
    return 0 <= row_idx < map_size and 0 <= col_idx < map_size

def tree_grow():
    tmp = [[0] * map_size for _ in range(map_size)]
    for row_idx in range(map_size):
        for col_idx in range(map_size):
            tmp[row_idx][col_idx] = total_map[row_idx][col_idx]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for row_idx in range(map_size):
        for col_idx in range(map_size):
            if total_map[row_idx][col_idx] > 0:
                grow_amount = 0
                for idx in range(4):
                    next_row_idx = row_idx + dx[idx]
                    next_col_idx = col_idx + dy[idx]
                    if in_range(next_row_idx, next_col_idx) and total_map[next_row_idx][next_col_idx] > 0:
                        grow_amount += 1
                tmp[row_idx][col_idx] += grow_amount

    for row_idx in range(map_size):
        for col_idx in range(map_size):
            total_map[row_idx][col_idx] = tmp[row_idx][col_idx]

def tree_spread():
    tmp = [[0] * map_size for _ in range(map_size)]
    for row_idx in range(map_size):
        for col_idx in range(map_size):
            tmp[row_idx][col_idx] = total_map[row_idx][col_idx]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for row_idx in range(map_size):
        for col_idx in range(map_size):
            if total_map[row_idx][col_idx] > 0:
                possible_region = 0
                possible_index = []
                for idx in range(4):
                    next_row_idx = row_idx + dx[idx]
                    next_col_idx = col_idx + dy[idx]
                    if in_range(next_row_idx, next_col_idx) and total_map[next_row_idx][next_col_idx] == 0:
                        possible_region += 1
                        possible_index.append(idx)
                if possible_region > 0:
                    grow_amount = total_map[row_idx][col_idx] // possible_region
                    for idx in possible_index:
                        tmp[row_idx+dx[idx]][col_idx+dy[idx]] += grow_amount
    
    for row_idx in range(map_size):
        for col_idx in range(map_size):
            total_map[row_idx][col_idx] = tmp[row_idx][col_idx]

def kill_start():
    result = 0

    for row_idx in range(map_size):
        for col_idx in range(map_size):
            if -INF < total_map[row_idx][col_idx] < 0:
                total_map[row_idx][col_idx] += 1

    cur_max = 0
    cur_max_row, cur_max_col = 0, 0
    tmp = [[0] * map_size for _ in range(map_size)]

    dx = [-1, -1, 1, 1]
    dy = [-1, 1, 1, -1]

    for row_idx in range(map_size):
        for col_idx in range(map_size):
            if total_map[row_idx][col_idx] > 0:
                tmp[row_idx][col_idx] += total_map[row_idx][col_idx]
                for idx in range(4):
                    for range_idx in range(kill_range):
                        next_row_idx = row_idx + dx[idx] * (range_idx+1)
                        next_col_idx = col_idx + dy[idx] * (range_idx+1)
                        if in_range(next_row_idx, next_col_idx):
                            if total_map[next_row_idx][next_col_idx] <= 0:
                                break
                            else:
                                tmp[row_idx][col_idx] += total_map[next_row_idx][next_col_idx]

    for row_idx in range(map_size):
        for col_idx in range(map_size):
            if cur_max < tmp[row_idx][col_idx]:
                cur_max_row = row_idx
                cur_max_col = col_idx
                cur_max = tmp[row_idx][col_idx]

    if total_map[cur_max_row][cur_max_col] == 0:
        return 0
    else:
        result += total_map[cur_max_row][cur_max_col]
        total_map[cur_max_row][cur_max_col] = -kill_remain
        for idx in range(4):
            for range_idx in range(kill_range):
                next_row_idx = cur_max_row + dx[idx] * (range_idx+1)
                next_col_idx = cur_max_col + dy[idx] * (range_idx+1)
                if in_range(next_row_idx, next_col_idx):
                    if -INF <= total_map[next_row_idx][next_col_idx] <= 0:
                        if total_map[next_row_idx][next_col_idx] == -INF:
                            pass
                        else:
                            total_map[next_row_idx][next_col_idx] = -kill_remain
                        break
                    else:
                        result += total_map[next_row_idx][next_col_idx]
                        total_map[next_row_idx][next_col_idx] = -kill_remain
    return result

# visualize()
result = 0
for turn_idx in range(total_turn):

    tree_grow()
    tree_spread()
    result += kill_start()
#     print(f"cumulated kill: {result}")

# visualize()
print(result)