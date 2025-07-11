import time

total_testcase = int(input())

dir_dict = {"U": 0, "D": 1, "R": 2, "L": 3}
dir_str_dict = {0: "^", 1: "v", 2: ">", 3: "<"}
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

INF = int(1e9)


def visualize(ball_list, min_x, max_x, min_y, max_y):
    print(f"<x: {min_x}~{max_x} / y: {min_y}~{max_y}>")
    total_map_ball_idx = [["x"] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    total_map_ball_dir = [["x"] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for ball_idx, cur_ball_list in enumerate(ball_list):
        cur_y = cur_ball_list[1]
        cur_x = cur_ball_list[0]
        cur_weight = cur_ball_list[2]
        cur_idx = cur_ball_list[-1]
        cur_dir = dir_str_dict[cur_ball_list[-2]]
        total_map_ball_idx[max_y - cur_y][cur_x - min_x] = cur_idx
        total_map_ball_dir[max_y - cur_y][cur_x - min_x] = cur_dir

    for row in total_map_ball_idx:
        print('\t'.join(map(str, row)))
    print()
    for row in total_map_ball_dir:
        print('\t'.join(map(str, row)))
    print()
    print()


def move(ball_list, min_x, max_x, min_y, max_y):
    hit = False
    next_ball_list = []
    # now = time.time()
    # tmp_map = [["x"] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for cur_ball_list in ball_list:
        # x, y, weight, direction, ball_idx
        cur_x, cur_y, cur_weight, cur_dir, cur_idx = cur_ball_list[0], cur_ball_list[1], cur_ball_list[2], cur_ball_list[3], cur_ball_list[4]
        next_x = cur_x + dx[cur_dir]
        next_y = cur_y + dy[cur_dir]

        if min_x <= next_x <= max_x and min_y <= next_y <= max_y:
            if tmp_map[max_y - next_y][next_x - min_x] == "x":
                tmp_map[max_y - next_y][next_x - min_x] = [next_x, next_y, cur_weight, cur_dir, cur_idx]
                next_ball_list.append([next_x, next_y, cur_weight, cur_dir, cur_idx])
            else:
                hit = True
                other_ball_list = tmp_map[max_y - next_y][next_x - min_x]
                other_ball_weight, other_ball_idx = other_ball_list[2], other_ball_list[-1]
                if other_ball_weight < cur_weight:
                    tmp_map[max_y - next_y][next_x - min_x] = [next_x, next_y, cur_weight, cur_dir, cur_idx]
                    for idx, _ball_list in enumerate(next_ball_list):
                        if _ball_list[-1] == other_ball_idx:
                            next_ball_list[idx] = [next_x, next_y, cur_weight, cur_dir, cur_idx]
                elif other_ball_weight == cur_weight:
                    if cur_idx > other_ball_idx:
                        tmp_map[max_y - next_y][next_x - min_x] = [next_x, next_y, cur_weight, cur_dir, cur_idx]
                        for idx, _ball_list in enumerate(next_ball_list):
                            if _ball_list[-1] == other_ball_idx:
                                next_ball_list[idx] = [next_x, next_y, cur_weight, cur_dir, cur_idx]

    for _ball_list in next_ball_list:
        tmp_map[max_y - _ball_list[1]][_ball_list[0] - min_x] = "x"
    # print(time.time()-now)

    # for y in range(max_y - min_y + 1):
    #     for x in range(max_x - min_x + 1):
    #         if tmp_map[y][x] != "x":
    #             next_ball_list.append(tmp_map[y][x])
    #             tmp_map[y][x] = "x"

    return hit, next_ball_list


def check(ball_list, min_x, max_x, min_y, max_y):
    return (len(ball_list) == 0)


for testcase_idx in range(total_testcase):
    total_ball = int(input())
    ball_list = []
    min_x, max_x, min_y, max_y = INF, -INF, INF, -INF
    for ball_idx in range(total_ball):
        cur_ball_info = list(input().split())
        cur_ball_dir = dir_dict[cur_ball_info[-1]]
        min_x = min(min_x, int(cur_ball_info[0]))
        max_x = max(max_x, int(cur_ball_info[0]))
        min_y = min(min_y, int(cur_ball_info[1]))
        max_y = max(max_y, int(cur_ball_info[1]))
        cur_ball_info_list = [int(cur_ball_info[0]), int(cur_ball_info[1]), int(cur_ball_info[2]), cur_ball_dir,
                              ball_idx]  # x, y, weight, direction, ball_idx
        ball_list.append(cur_ball_info_list)
    for ball_idx, cur_ball_list in enumerate(ball_list):
        cur_ball_list[0] = min_x + (cur_ball_list[0] - min_x) * 2
        cur_ball_list[1] = min_y + (cur_ball_list[1] - min_y) * 2

    max_x = min_x + (max_x - min_x) * 2
    max_y = min_y + (max_y - min_y) * 2

    result = -1
    cur_time = 0
    # visualize(ball_list, min_x, max_x, min_y, max_y)
    tmp_map = [["x"] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    while True:
        # now = time.time()
        cur_time += 1

        hit, ball_list = move(ball_list, min_x, max_x, min_y, max_y)
        if hit:
            result = cur_time

        if check(ball_list, min_x, max_x, min_y, max_y):
            break
        # print(time.time()-now)
    print(result)
    del tmp_map
    del cur_ball_info
    