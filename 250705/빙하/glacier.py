from collections import deque

num_row, num_col = map(int, input().split())

total_map = []
for _ in range(num_row):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)

def check_water():
    result = [[False] * num_col for _ in range(num_row)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([(0, 0)])
    result[0][0] = True
    while queue:
        cur_node = queue.popleft()
        cur_row, cur_col = cur_node[0], cur_node[1]
        for idx in range(4):
            next_row = cur_row + dx[idx]
            next_col = cur_col + dy[idx]
            if next_row >= 0 and next_row < num_row and next_col >= 0 and next_col < num_col and not result[next_row][next_col] \
                and total_map[next_row][next_col] == 0:
                result[next_row][next_col] = True
                queue.append((next_row, next_col))
    return result

def melt_ice(available_water):
    result = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for row_idx in range(num_row):
        for col_idx in range(num_col):
            if available_water[row_idx][col_idx]:
                for idx in range(4):
                    next_row = row_idx + dx[idx]
                    next_col = col_idx + dy[idx]
                    if next_row >= 0 and next_row < num_row and next_col >= 0 and next_col < num_col and \
                        total_map[next_row][next_col] == 1:
                        total_map[next_row][next_col] = 0
                        result += 1
    return result

def check_end():
    for row_idx in range(num_row):
        for col_idx in range(num_col):
            if total_map[row_idx][col_idx] == 1:
                return False
    return True

time = 0
while True:
    time += 1
    available_water = check_water()
    result = melt_ice(available_water)
    if check_end():
        print(f"{time} {result}")
        break
