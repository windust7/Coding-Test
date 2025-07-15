from collections import deque

map_size, people_num, shelter_num = map(int, input().split())

total_map = []
people_list = []
for row_idx in range(map_size):
    cur_row = list(map(int, input().split()))
    total_map.append(cur_row)
    if 2 in cur_row:
        for col_idx in range(map_size):
            if cur_row[col_idx] == 2:
                people_list.append([row_idx, col_idx])
assert len(people_list) == people_num

result = [[0] * map_size for _ in range(map_size)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for person_idx, person in enumerate(people_list):
    cur_row, cur_col = person[0], person[1]
    queue = deque([[cur_row, cur_col]])
    visited = [[0] * map_size for _ in range(map_size)]
    found = False
    while queue:
        cur_node = queue.popleft()
        cur_row, cur_col = cur_node[0], cur_node[1]
        for idx in range(4):
            next_row = cur_row + dx[idx]
            next_col = cur_col + dy[idx]
            if 0 <= next_row < map_size and 0 <= next_col < map_size and visited[next_row][next_col] == 0 and not ((next_row, next_col) == (person[0], person[1])) and total_map[next_row][next_col] != 1:
                if total_map[next_row][next_col] == 3:
                    result[person[0]][person[1]] = visited[cur_row][cur_col] + 1
                    found = True
                else:
                    visited[next_row][next_col] = visited[cur_row][cur_col] + 1
                    queue.append([next_row, next_col])
        if found:
            break
    if not found:
        result[person[0]][person[1]] = -1

for row in result:
    print(" ".join(map(str, row)))
