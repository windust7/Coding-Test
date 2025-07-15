"""
nxn map

m명의 사람이 빵을 찾음
1번 사람은 1분에, ... , m번 사람은 m분에 각자 위치에서 출발
    출발 전에는 격자 밖에 있음
    각자 목표로 하는 편의점이 다름

각자 1분동안 움직이는 규칙:
    1. 본인이 가고 싶은 편의점 방향으로 1칸 움직임.
        1-1. 최단 거리로 움직이는 방법이 여러가지라면 북서동남의 우선순위
    2. 편의점에 도착한다면 해당 편의점에서 멈춘다
        2-1. 다른 사람들은 이 편의점을 지나갈 수 없다
            2-1-1. 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없다
    3. 현재 시간이 t분일 때, t <= m이면 t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어간다.
        3-1. 가장 가까운 베이스캠프가 여러개면 행이 작은거, 행도 같다면 열이 작은거
        3-2. 이때부터 다른 사람들은 해당 베이스 캠프가 있는 칸을 지나갈 수 없다.
            3-2-1. 해당 턴 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없다.
"""

"""
무조건 도달 가능함
그러면 최대로 걸리는 시간은 n^2 -> 225
사람의 수는 최대 30

매 턴마다 BFS를 돌리면 안되나?
    즉 매 턴마다 225 * 30 -> 6750 (모든 사람에 대해서 BFS)
전체 턴: 6750 * 225
"""

from collections import deque

map_size, people_num = map(int, input().split())
total_map = []
basecamp_list = []
target_list = []
people_list = []
people_succeed = [False for _ in range(people_num)]
for row_idx in range(map_size):
    cur_row = list(map(int, input().split()))
    for col_idx in range(map_size):
        if cur_row[col_idx] == 1:
            basecamp_list.append([row_idx, col_idx])
    total_map.append(cur_row)
for person_idx in range(people_num):
    target_row, target_col = map(int, input().split())
    target_list.append([target_row-1, target_col-1])

def in_range(row_idx, col_idx):
    return 0 <= row_idx < map_size and 0 <= col_idx < map_size

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

unavailable_map = [[False] * map_size for _ in range(map_size)]

current_time = 0
while True:
    current_time += 1

    # 1번 움직임
    if current_time > 1:
        people_move_plan = [None for _ in range(people_num)]
        for person_idx, person in enumerate(people_list):
            if not people_succeed[person_idx]:
                found = False
                min_dist = None
                visited = [[0] * map_size for _ in range(map_size)]
                target_row, target_col = person[0], person[1]
                cur_row, cur_col = target_list[person_idx][0], target_list[person_idx][1]
                queue = deque([[cur_row, cur_col]])
                while queue:
                    cur_node = queue.popleft()
                    cur_row, cur_col = cur_node[0], cur_node[1]
                    for idx in range(4):
                        next_row, next_col = cur_row + dx[idx], cur_col + dy[idx]
                        if in_range(next_row, next_col) and visited[next_row][next_col] == 0 and not ((next_row, next_col) == (target_list[person_idx][0], target_list[person_idx][1])) and not unavailable_map[next_row][next_col]:
                            visited[next_row][next_col] = visited[cur_row][cur_col] + 1
                            if next_row == target_row and next_col == target_col:
                                found = True
                                if min_dist is None:
                                    min_dist = visited[next_row][next_col]
                            else:
                                if not found:
                                    queue.append([next_row, next_col])
                                else:
                                    if visited[next_row][next_col] < min_dist:
                                        queue.append([next_row, next_col])
            people_move_plan[person_idx] = visited
        for person_idx, person in enumerate(people_list):
            if not people_succeed[person_idx]:
                my_move_plan = people_move_plan[person_idx]
                target_row, target_col = target_list[person_idx][0], target_list[person_idx][1]
                cur_row, cur_col = person[0], person[1]
                for idx in range(4):
                    next_row, next_col = cur_row + dx[idx], cur_col + dy[idx]
                    if in_range(next_row, next_col) and (my_move_plan[next_row][next_col] > 0 or (next_row, next_col) == (target_row, target_col)):
                        people_list[person_idx] = [next_row, next_col]
                        break

    # 2번 움직임
    if current_time > 1:
        for person_idx, person in enumerate(people_list):
            if not people_succeed[person_idx]:
                if (person[0], person[1]) == (target_list[person_idx][0], target_list[person_idx][1]):
                    unavailable_map[person[0]][person[1]] = True
                    people_succeed[person_idx] = True

    # 3번 움직임
    if current_time <= people_num:
        # people_list를 늘려줘야 함
        cur_target = target_list[current_time-1]
        cur_target_row, cur_target_col = cur_target[0], cur_target[1]
        road_to_basecamp = [[0] * map_size for _ in range(map_size)]
        queue = deque([[cur_target_row, cur_target_col]])
        found = False
        min_dist = None
        while queue:
            cur_node = queue.popleft()
            cur_row, cur_col = cur_node[0], cur_node[1]
            for idx in range(4):
                next_row, next_col = cur_row + dx[idx], cur_col + dy[idx]
                if in_range(next_row, next_col) and not unavailable_map[next_row][next_col] and road_to_basecamp[next_row][next_col] == 0 and not ((next_row, next_col) == (cur_target_row, cur_target_col)):
                    road_to_basecamp[next_row][next_col] = road_to_basecamp[cur_row][cur_col] + 1
                    if [next_row, next_col] in basecamp_list:
                        found = True
                        if min_dist is None:
                            min_dist = road_to_basecamp[next_row][next_col]
                    else:
                        if not found:
                            queue.append([next_row, next_col])
                        else:
                            if road_to_basecamp[next_row][next_col] < min_dist:
                                queue.append([next_row, next_col])
        for row_idx in range(map_size):
            for col_idx in range(map_size):
                if not unavailable_map[row_idx][col_idx] and [row_idx, col_idx] in basecamp_list and road_to_basecamp[row_idx][col_idx] != 0:
                    people_list.append([row_idx, col_idx])
                    unavailable_map[row_idx][col_idx] = True
                    break
            if len(people_list) == current_time:
                break
    else:
        all_suceed = True
        for suc in people_succeed:
            if not suc:
                all_suceed = False
                break
        if all_suceed:
            print(current_time)
            break