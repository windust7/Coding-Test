"""
N x M 격자가 있고 모든 위치에 포탑이 존재함
각 포탑은 공격력이 존재함.
공격력이 0 이하가 되면 해당 포탑은 부서지고 더 이상 공격을 못함
최초에 0인 포탑 또한 존재할 수 있다

각 턴마다:
    1. 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정
        1-1. 그 포탑은 N + M 만큼의 공격력이 증가
        1-2. 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑
            1-2-1. 모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정
            1-2-2. 만약 가장 최근에 공격한 포탑이 2개 이상이면, 각 포탑 위치의 행과 열의 합이 가장 큰 포탑
                1-2-2-1. 만약 행과 열의 합이 가장 큰게 2개 이상이면, 열 값이 가장 큰 포탑

    2. 선정된 공격자는 자신을 제외한 가장 강한 포탑을 공격
        2-1. 1번에서 정한 기준의 반대
        2-2. 레이저 공격:
            2-2-1. 상하좌우의 4개의 방향으로 움직일 수 있다
            2-2-2. 부서진 포탑이 있는 위치는 지날 수 없다
            2-2-3. 가장자리에서 막힌 방향으로 진행하고자 하면, 반대편으로 나온다.
            2-2-4. 공격자의 위치에서 공격 대상 포탑까지의 최단 경로로 공격. 경로가 없으면 포탄 공격을 진행함.
            2-2-5. 최단 경로가 2개 이상이면, 우하좌상의 순위대로
            2-2-6. 공격 대상에는 공격자의 공격력만큼의 피해를 입히며, 피해를 입은 포탑은 해당 수치만큼 공격력이 줄어든다.
            2-2-7. 공격 대상을 제외한 레이저 경로에 있는 포탑도 공격을 받음. 공격자 공격력의 절반 반큼만
        2-3: 포탄 공격:
            2-3-1. 공격 대상은 공격자 공격력 만큼의 피해를 받음.
            2-3-2. 공격 대상의 주위 8개 방향에 있는 포탑은 공격자 공격력의 절반 만큼의 피해를 받음.
            2-3-3. 공격자는 해당 공격에 영향을 받지 않는다
            2-3-4. 만약 가장자리에 포탄이 떨어진다면, 포탄의 추가 피해가 반대편 격자에 미치게 된다.

    3. 포탑 부서짐

    4. 포탑 정비
        4-1. 부서지지 않은 포탑 중 공격자와 공격에 피해를 입은 포탑이 아닌 것들은 공격력이 1씩 올라간다.
"""

"""
각 포탑별로: (공격력, 가장 최근에 공격했던 turn index, row_idx, col_idx, 부서졌는지 여부, 공격자 flag, 공격 대상 flag)
2차원 맵에 이 포탑의 list를 정의함

1: 그냥 sort(key=...)?
"""

from collections import deque

CHECK = False

num_row, num_col, num_turn = map(int, input().split())

total_map = [[None] * num_col for _ in range(num_row)]
alive_player_list = []
for row_idx in range(num_row):
    cur_row = list(map(int, input().split()))
    for col_idx in range(num_col):
        # 공격력, 최근 공격했던 turn, row_idx, col_idx, 부서졌는지 여부, 공격자 flag, 공격 대상 flag
        cur_player = [cur_row[col_idx], 0, row_idx, col_idx, int(cur_row[col_idx] == 0), False, False]
        total_map[row_idx][col_idx] = cur_player
        if cur_row[col_idx] != 0:
            alive_player_list.append(cur_player)

def visualize():
    power_map = [[None] * num_col for _ in range(num_row)]
    last_turn_map = [[None] * num_col for _ in range(num_row)]
    broken_map = [[None] * num_col for _ in range(num_row)]
    attacker_map = [[False] * num_col for _ in range(num_row)]
    target_map = [[False] * num_col for _ in range(num_row)]
    for row_idx in range(num_row):
        for col_idx in range(num_col):
            cur_player = tuple(total_map[row_idx][col_idx])
            power, last_turn, _, _, is_broken, is_attacker, is_target = cur_player
            power_map[row_idx][col_idx] = power
            last_turn_map[row_idx][col_idx] = last_turn
            broken_map[row_idx][col_idx] = is_broken
            attacker_map[row_idx][col_idx] = is_attacker
            target_map[row_idx][col_idx] = is_target

    print("power:")
    for row in power_map:
        print('\t'.join(map(str, row)))
    print()

    print("last turn:")
    for row in last_turn_map:
        print('\t'.join(map(str, row)))
    print()

    print("broken:")
    for row in broken_map:
        print('\t'.join(map(str, row)))
    print()

    print("attacker:")
    for row in attacker_map:
        print('\t'.join(map(str, row)))
    print()

    print("target:")
    for row in target_map:
        print('\t'.join(map(str, row)))
    print()

    print()

if CHECK:
    visualize()

def choose_attacker():

    alive_player_list.sort(key=lambda x: (x[0], -x[1], -(x[2] + x[3]), -x[3]))

    attacker = alive_player_list[0]

    attacker[0] += (num_row + num_col)
    attacker[5] = True

    return attacker

def choose_target():

    alive_player_list.sort(key=lambda x: (-x[0], x[1], (x[2] + x[3]), x[3]))

    target = alive_player_list[0]

    if target[5]:
        target = alive_player_list[1]

    target[6] = True

    return target

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(start_row_idx, start_col_idx, end_row_idx, end_col_idx):
    result_map = [[None] * num_col for _ in range(num_row)]

    queue = deque([[end_row_idx, end_col_idx]])
    result_map[end_row_idx][end_col_idx] = 0

    while queue:
        cur_node = queue.popleft()
        cur_row_idx, cur_col_idx = cur_node[0], cur_node[1]
        for idx in range(4):
            next_row_idx, next_col_idx = (cur_row_idx + dx[idx] + num_row) % num_row, (cur_col_idx + dy[idx] + num_col) % num_col
            if total_map[next_row_idx][next_col_idx][4]:
                continue
            elif result_map[next_row_idx][next_col_idx] is None:
                result_map[next_row_idx][next_col_idx] = result_map[cur_row_idx][cur_col_idx] + 1
                queue.append([next_row_idx, next_col_idx])

    if result_map[start_row_idx][start_col_idx] is None:
        return result_map, False
    else:
        return result_map, True

def attack_and_break(attacker, target):
    result_map, is_available = bfs(attacker[2], attacker[3], target[2], target[3])
    if is_available:
        # 레이저 공격
        cur_row_idx, cur_col_idx = attacker[2], attacker[3]
        while True:
            next_move_idx = 0
            min_dist = int(1e9)
            for idx in range(4):
                next_row_idx = (cur_row_idx + dx[idx] + num_row) % num_row
                next_col_idx = (cur_col_idx + dy[idx] + num_col) % num_col
                if result_map[next_row_idx][next_col_idx] is not None:
                    if min_dist > result_map[next_row_idx][next_col_idx]:
                        min_dist = result_map[next_row_idx][next_col_idx]
                        next_move_idx = idx
            next_row_idx = (cur_row_idx + dx[next_move_idx] + num_row) % num_row
            next_col_idx = (cur_col_idx + dy[next_move_idx] + num_col) % num_col

            if next_row_idx == target[2] and next_col_idx == target[3]:
                target[0] -= attacker[0]
                if target[0] <= 0:
                    target[0] = 0
                    target[4] = True
                    alive_player_list.remove(target)
                break
            else:
                total_map[next_row_idx][next_col_idx][0] -= (attacker[0] // 2)
                if total_map[next_row_idx][next_col_idx][0] <= 0:
                    total_map[next_row_idx][next_col_idx][0] = 0
                    total_map[next_row_idx][next_col_idx][4] = True
                    alive_player_list.remove(total_map[next_row_idx][next_col_idx])
                else:
                    # 나중에 4. 포탑 정비에서 다시 +1 됨
                    total_map[next_row_idx][next_col_idx][0] -= 1
                cur_row_idx = next_row_idx
                cur_col_idx = next_col_idx

    else:
        _dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        _dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        cur_row_idx, cur_col_idx = target[2], target[3]
        target[0] -= attacker[0]
        if target[0] <= 0:
            target[0] = 0
            target[4] = True
            alive_player_list.remove(target)
        for idx in range(8):
            next_row_idx = (cur_row_idx + _dx[idx] + num_row) % num_row
            next_col_idx = (cur_col_idx + _dy[idx] + num_col) % num_col
            if not total_map[next_row_idx][next_col_idx][5]:
                total_map[next_row_idx][next_col_idx][0] -= (attacker[0] // 2)
                if total_map[next_row_idx][next_col_idx][0] <= 0:
                    total_map[next_row_idx][next_col_idx][0] = 0
                    total_map[next_row_idx][next_col_idx][4] = True
                    if total_map[next_row_idx][next_col_idx] in alive_player_list:
                        alive_player_list.remove(total_map[next_row_idx][next_col_idx])
                else:
                    # 나중에 4. 포탑 정비에서 다시 +1 됨
                    total_map[next_row_idx][next_col_idx][0] -= 1

def power_up_and_initialize():
    for row_idx in range(num_row):
        for col_idx in range(num_col):
            cur_player = total_map[row_idx][col_idx]
            if not cur_player[-2] and not cur_player[-1] and not cur_player[-3]:
                cur_player[0] += 1
            if cur_player[-2]:
                cur_player[-2] = False
            if cur_player[-1]:
                cur_player[-1] = False

def find_biggest_power():
    return_value = 0
    for row_idx in range(num_row):
        for col_idx in range(num_col):
            return_value = max(total_map[row_idx][col_idx][0], return_value)
    return return_value

# 공격력, 최근 공격했던 turn, row_idx, col_idx, 부서졌는지 여부, 공격자 flag, 공격 대상 flag

for cur_turn in range(1, num_turn+1):

    if CHECK:
        print(f"current turn: {cur_turn}\n")

    attacker = choose_attacker()
    attacker[1] = cur_turn

    if CHECK:
        print("choose_attacker")
        visualize()

    target = choose_target()

    if CHECK:
        print("choose_target")
        visualize()

    attack_and_break(attacker, target)

    if CHECK:
        print("attack_and_break")
        visualize()

    power_up_and_initialize()

    if CHECK:
        print("power_up_and_initialize")
        visualize()

    if len(alive_player_list) == 1:
        break

biggest_power = find_biggest_power()
print(biggest_power)