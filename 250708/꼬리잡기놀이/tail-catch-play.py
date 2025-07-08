from collections import deque

map_size, team_num, total_turn = map(int, input().split())

team_header_list = [[] for _ in range(team_num)]
team_trailer_list = [[] for _ in range(team_num)]
cur_team_idx = 0
total_map = []
for row_idx in range(map_size):
    cur_row = list(map(int, input().split()))
    if 1 in cur_row:
        for col_idx in range(map_size):
            if cur_row[col_idx] == 1:
                team_header_list[cur_team_idx].extend([row_idx, col_idx])
                cur_team_idx += 1
    total_map.append(cur_row)
assert cur_team_idx == team_num, "the number of 1 is not equal to the number of total team"

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for team_idx, header in enumerate(team_header_list):
    visited = [[False] * map_size for _ in range(map_size)]
    header_row, header_col = header[0], header[1]
    queue = deque([[header_row, header_col]])
    visited[header_row][header_col] = True
    while queue:
        cur_node = queue.popleft()
        cur_row, cur_col = cur_node[0], cur_node[1]
        for idx in range(4):
            next_row = cur_row + dx[idx]
            next_col = cur_col + dy[idx]
            if 0 <= next_row < map_size and 0 <= next_col < map_size and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                if total_map[next_row][next_col] == 2:
                    queue.append([next_row, next_col])
                elif total_map[next_row][next_col] == 3:
                    team_trailer_list[team_idx].extend([next_row, next_col])


# print(team_header_list)
# print(team_trailer_list)

def in_range(row_idx, col_idx):
    return 0 <= row_idx < map_size and 0 <= col_idx < map_size


def move_forward():
    tmp = [[False] * map_size for _ in range(map_size)]
    for row_idx in range(map_size):
        for col_idx in range(map_size):
            tmp[row_idx][col_idx] = total_map[row_idx][col_idx]
    team_idx = 0
    for header, trailer in zip(team_header_list, team_trailer_list):
        header_row, header_col, trailer_row, trailer_col = header[0], header[1], trailer[0], trailer[1]
        for idx in range(4):
            next_header_row = header_row + dx[idx]
            next_header_col = header_col + dy[idx]
            if in_range(next_header_row, next_header_col) and (
                    total_map[next_header_row][next_header_col] == 3 or total_map[next_header_row][
                next_header_col] == 4):
                tmp[next_header_row][next_header_col] = 1
                tmp[header_row][header_col] = 2
                team_header_list[team_idx] = [next_header_row, next_header_col]
                break
        for idx in range(4):
            next_trailer_row = trailer_row + dx[idx]
            next_trailer_col = trailer_col + dy[idx]
            if in_range(next_trailer_row, next_trailer_col) and total_map[next_trailer_row][next_trailer_col] == 2:
                tmp[next_trailer_row][next_trailer_col] = 3
                if tmp[trailer_row][trailer_col] == 1:
                    pass
                else:
                    tmp[trailer_row][trailer_col] = 4
                team_trailer_list[team_idx] = [next_trailer_row, next_trailer_col]
                break
        team_idx += 1
    for row_idx in range(map_size):
        for col_idx in range(map_size):
            total_map[row_idx][col_idx] = tmp[row_idx][col_idx]


def move_ball(ball_row, ball_col, ball_dir):
    hit = False
    hit_row, hit_col = None, None
    while True:
        ball_row += dx[ball_dir]
        ball_col += dy[ball_dir]
        if not in_range(ball_row, ball_col):
            break
        if total_map[ball_row][ball_col] == 1 or total_map[ball_row][ball_col] == 2 or total_map[ball_row][
            ball_col] == 3:
            hit = True
            hit_row, hit_col = ball_row, ball_col
            break
    return hit, hit_row, hit_col


def cal_score(row_idx, col_idx):
    """
    맞은 사람이 1, 2, 3 중에 어디에 속하는지 보고 점수 계산하고 그 팀 방향 바꾸기 (header와 trailer 바꾸기)
    """
    to_header_list = []
    to_trailer_list = []
    cur_row, cur_col = row_idx, col_idx

    def dfs(cur_row_idx, cur_col_idx, cur_depth, cur_visited):
        if total_map[cur_row_idx][cur_col_idx] == 1 or total_map[cur_row_idx][cur_col_idx] == 3:
            return (cur_depth, total_map[cur_row_idx][cur_col_idx], cur_row_idx, cur_col_idx)
        else:
            cur_visited[cur_row_idx][cur_col_idx] = True
            for idx in range(4):
                next_row_idx = cur_row_idx + dx[idx]
                next_col_idx = cur_col_idx + dy[idx]
                if in_range(next_row_idx, next_col_idx) and not cur_visited[next_row_idx][next_col_idx] and \
                        total_map[next_row_idx][next_col_idx] != 0:
                    result_tuple = dfs(next_row_idx, next_col_idx, cur_depth + 1, cur_visited)
            return result_tuple
    # breakpoint()
    if total_map[cur_row][cur_col] == 1:
        visited = [[False] * map_size for _ in range(map_size)]
        visited[cur_row][cur_col] = True
        for idx in range(4):
            next_row_idx = cur_row + dx[idx]
            next_col_idx = cur_col + dy[idx]
            if in_range(next_row_idx, next_col_idx) and total_map[next_row_idx][next_col_idx] == 2:
                result_tuple = dfs(next_row_idx, next_col_idx, 2, visited)
        score = 1
        head_row, head_col = cur_row, cur_col
    elif total_map[cur_row][cur_col] == 3:
        visited = [[False] * map_size for _ in range(map_size)]
        visited[cur_row][cur_col] = True
        for idx in range(4):
            next_row_idx = cur_row + dx[idx]
            next_col_idx = cur_col + dy[idx]
            if in_range(next_row_idx, next_col_idx) and total_map[next_row_idx][next_col_idx] == 2:
                result_tuple = dfs(next_row_idx, next_col_idx, 2, visited)
        score = result_tuple[0] ** 2
        head_row, head_col = result_tuple[-2], result_tuple[-1]
    else:
        for idx in range(4):
            next_row_idx = cur_row + dx[idx]
            next_col_idx = cur_col + dy[idx]
            if in_range(next_row_idx, next_col_idx) and total_map[next_row_idx][next_col_idx] != 0:
                visited = [[False] * map_size for _ in range(map_size)]
                visited[next_row_idx][next_col_idx] = True
                visited[cur_row][cur_col] = True
                result_tuple = dfs(next_row_idx, next_col_idx, 2, visited)
                break
        for idx in range(4):
            next_row_idx = cur_row + dx[idx]
            next_col_idx = cur_col + dy[idx]
            if in_range(next_row_idx, next_col_idx) and total_map[next_row_idx][next_col_idx] != 0 and not \
            visited[next_row_idx][next_col_idx]:
                visited[next_row_idx][next_col_idx] = True
                result_tuple_2 = dfs(next_row_idx, next_col_idx, 2, visited)
        if result_tuple[1] == 1:
            score = result_tuple[0] ** 2
            head_row, head_col = result_tuple[-2], result_tuple[-1]
        else:
            score = result_tuple_2[0] ** 2
            head_row, head_col = result_tuple_2[-2], result_tuple_2[-1]

    for idx in range(len(team_header_list)):
        if team_header_list[idx][0] == head_row and team_header_list[idx][1] == head_col:
            total_map[team_header_list[idx][0]][team_header_list[idx][1]] = 3
            total_map[team_trailer_list[idx][0]][team_trailer_list[idx][1]] = 1
            team_header_list[idx], team_trailer_list[idx] = team_trailer_list[idx], team_header_list[idx]
            break

    return score


result = 0
for turn_idx in range(total_turn):
    move_forward()

    turn_idx = (turn_idx) % (4 * map_size)
    if 0 <= turn_idx < map_size:
        start_ball_row = turn_idx
        start_ball_col = 0
        ball_dir = 0
    elif map_size <= turn_idx < 2 * map_size:
        start_ball_row = map_size - 1
        start_ball_col = turn_idx - map_size
        ball_dir = 1
    elif 2 * map_size <= turn_idx < 3 * map_size:
        start_ball_row = map_size - (turn_idx - 2 * map_size) - 1
        start_ball_col = map_size - 1
        ball_dir = 2
    elif 3 * map_size <= turn_idx < 4 * map_size:
        start_ball_row = 0
        start_ball_col = map_size - (turn_idx - 3 * map_size) - 1
        ball_dir = 3
    hitted, score_row, score_col = move_ball(start_ball_row, start_ball_col, ball_dir)
    if hitted:
        result += cal_score(score_row, score_col)
    # 
    # for row in total_map:
    #     print(row)
    # print()

print(result)

"""
1. 각 team별로 header, trailer 찾기
(이후 각 turn마다)
2. 한 칸 이동
3. 공 던지고 맞은 사람 찾기
4. 맞은 사람이 1, 2, 3 중에 어디에 속하는지 보고 점수 계산하고 그 팀 방향 바꾸기 (header와 trailer 바꾸기)
"""