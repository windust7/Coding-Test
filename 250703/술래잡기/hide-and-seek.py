CHECK = False

map_size, num_target, num_tree, total_turn = map(int, input().split())
target_list = []
for _ in range(num_target):
    target_type = list(map(int, input().split()))
    target_type[0] -= 1
    target_type[1] -= 1
    if target_type[2] == 2:
        target_type[2] = 3  # 1: right, 2: left, 3: down, 4: up
    target_list.append(target_type)
tree_list = []
for _ in range(num_tree):
    tree_coord = list(map(int, input().split()))
    tree_coord[0] -= 1
    tree_coord[1] -= 1
    tree_list.append(tree_coord)

cur_row = (map_size - 1) // 2
cur_col = (map_size - 1) // 2

first_direction_map = [["*"] * map_size for _ in range(map_size)]
second_direction_map = [["*"] * map_size for _ in range(map_size)]
first_direction_map[cur_row][cur_col] = "^"
first_direction_map[0][0] = "^"
second_direction_map[cur_row][cur_col] = "v"
second_direction_map[0][0] = "v"

start_row = cur_row
start_col = cur_col
start_direction = 0
direction_length = 0
direction_list = []
for size in range(1, (map_size+1)):
    for _ in range(2):
        direction_list.append(size)
while not (start_row == 0 and start_col == 0):
    direction_str = ["^", ">", "v", "<"]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for _ in range(direction_list[direction_length]):
        first_direction_map[start_row][start_col] = direction_str[start_direction]
        start_row += dx[start_direction]
        start_col += dy[start_direction]
        if (start_row == 0 and start_col == 0):
            break
    start_direction = (start_direction + 1) % 4
    direction_length += 1

start_row = 0
start_col = 0
start_direction = 0
direction_length = 0
direction_list = []
for size in range((map_size-1), 0, -1):
    for _ in range(2):
        direction_list.append(size)
direction_list = [map_size-1] + direction_list
while not (start_row == cur_row and start_col == cur_col):
    direction_str = ["v", ">", "^", "<"]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for _ in range(direction_list[direction_length]):
        second_direction_map[start_row][start_col] = direction_str[start_direction]
        start_row += dx[start_direction]
        start_col += dy[start_direction]
        if (start_row == cur_row and start_col == cur_col):
            break
    start_direction = (start_direction + 1) % 4
    direction_length += 1

def visualize(target_list, tree_list, cur_row, cur_col):
    global map_size
    total_map = [["*"] * map_size for _ in range(map_size)]
    for tree in tree_list:
        if total_map[tree[0]][tree[1]] == "*":
            total_map[tree[0]][tree[1]] = "T"
        else:
            total_map[tree[0]][tree[1]] += "T"
    for target in target_list:
        direction_dict = {1: ">", 2: "<", 3: "v", 4: "^"}
        if total_map[target[0]][target[1]] == "*":
            total_map[target[0]][target[1]] = direction_dict[target[2]]
        else:
            total_map[target[0]][target[1]] += direction_dict[target[2]]
    if total_map[cur_row][cur_col] == "*":
        total_map[cur_row][cur_col] = "I"
    else:
        total_map[cur_row][cur_col] += "I"
    for row in total_map:
        print(row)
    print()

first_flag = True
result = 0
for turn_idx in range(total_turn):
    if CHECK:
        visualize(target_list, tree_list, cur_row, cur_col)
    # target turn
    # 1: right, 2: left, 3: down, 4: up
    dx = [None, 0, 0, 1, -1]
    dy = [None, 1, -1, 0, 0]
    for target_idx, target in enumerate(target_list):
        target_row, target_col, target_dir = target[0], target[1], target[2]
        if (abs(target_row - cur_row) + abs(target_col - cur_col)) <= 3:
            next_target_row = target_row + dx[target_dir]
            next_target_col = target_col + dy[target_dir]
            if next_target_row >= 0 and next_target_row < map_size and next_target_col >= 0 and next_target_col < map_size:
                if not (next_target_row == cur_row and next_target_col == cur_col):    
                    target[0] = next_target_row
                    target[1] = next_target_col
                    target_list[target_idx] = [target[0], target[1], target_dir]
            else:
                if target_dir == 1:
                    target_dir = 2
                elif target_dir == 2:
                    target_dir = 1
                elif target_dir == 3:
                    target_dir = 4
                elif target_dir == 4:
                    target_dir = 3
                next_target_row = target_row + dx[target_dir]
                next_target_col = target_col + dy[target_dir]
                if not (next_target_row == cur_row and next_target_col == cur_col):
                    target[0] = next_target_row
                    target[1] = next_target_col
                    target_list[target_idx] = [target[0], target[1], target_dir]

    # my turn
    if first_flag:
        my_dir = first_direction_map
    else:
        my_dir = second_direction_map
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    if my_dir[cur_row][cur_col] == "^":
        cur_dir = 0
    elif my_dir[cur_row][cur_col] == ">":
        cur_dir = 1
    elif my_dir[cur_row][cur_col] == "v":
        cur_dir = 2
    elif my_dir[cur_row][cur_col] == "<":
        cur_dir = 3
    cur_row = cur_row + dx[cur_dir]
    cur_col = cur_col + dy[cur_dir]
    if cur_row == 0 and cur_col == 0:
        first_flag = not first_flag
        if first_flag:
            my_dir = first_direction_map
        else:
            my_dir = second_direction_map
    elif (cur_row == (map_size - 1) // 2) and (cur_col == (map_size - 1) // 2):
        first_flag = not first_flag
        if first_flag:
            my_dir = first_direction_map
        else:
            my_dir = second_direction_map
    if my_dir[cur_row][cur_col] == "^":
        cur_dir = 0
    elif my_dir[cur_row][cur_col] == ">":
        cur_dir = 1
    elif my_dir[cur_row][cur_col] == "v":
        cur_dir = 2
    elif my_dir[cur_row][cur_col] == "<":
        cur_dir = 3
    check_row = cur_row
    check_col = cur_col
    for i in range(3):
        if i != 0:
            check_row = check_row + dx[cur_dir]
            check_col = check_col + dy[cur_dir]
        if check_row >= 0 and check_row < map_size and check_col >= 0 and check_col < map_size:
            tree_exist = False
            for tree in tree_list:
                if check_row == tree[0] and check_col == tree[1]:
                    tree_exist = True
            if not tree_exist:
                catch_target_idx_list = []
                for target_idx, target in enumerate(target_list):
                    if check_row == target[0] and check_col == target[1]:
                        result += (turn_idx+1)
                        catch_target_idx_list.append(target_idx)
                if len(catch_target_idx_list) >= 1:
                    catch_target_idx_list.reverse()
                    for idx in catch_target_idx_list:
                        target_list.pop(idx)

if CHECK:
    visualize(target_list, tree_list, cur_row, cur_col)

print(result)
