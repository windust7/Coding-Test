"""
1. 경주 시작 준비
    1-1. P마리의 토끼가 N x M 크기의 격자 위에 있음
    1-2. 각 토끼에게는 고유한 번호가 붙어있음. pid_i
    1-3. 각 토끼마다 한 번 움직일 때 꼭 이동해야 하는 거리도 정해져 있음 d_i
    1-4. 처음에는 모두 1행 1열에 있음

2. 경주 진행
    2-1. 가장 우선순위가 높은 토끼를 뽑아서 멀리 보내주는 것을 K번 반복
        2-1-1. 우선순위는 순서대로 (현재까지의 총 점프 횟수가 적은 토끼, 현재 서있는 행 번호 + 열 번호가 작은 토끼, 행 번호가 작은 토끼, 열 번호가 작은 토끼, 고유번호가 작은 토끼)
        
        2-2. 토끼가 결정이 되면 상하좌우 각각 d_i만큼 이동했을 때의 위치를 구한다
            2-2-1. 격자를 벗어나면 방향을 반대로 바꿔서 한 칸 이동
            2-2-2. 4개의 위치 중에서 (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 우선순위 중 가장 높은 칸을 골라 이동시킴
            2-2-3. 이 칸의 위치를 r_i, c_i라고 하면 나머지 토끼들은 r_i + c_i만큼의 점수를 동시에 얻음
                2-2-3-1. zero-base로 변환 해줘야 함!!!
    
    2-3. K번의 턴이 모두 진행된 직후에 (현재 서있는 행 번호 + 열 번호가 큰 토끼, 행 번호가 큰 토끼, 열 번호가 큰 토끼, 고유번호가 큰 토끼) 우선순위 중 가장 높은 토끼를 골라 점수 S를 더해줌.
        2-3-1. K번의 턴 동안 한번이라도 뽑혔던 적이 있었던 토끼중에서!

3. 이동거리 변경
    3-1. 고유번호가 pid_t인 토끼의 이동거리를 L배 해준다

4. 점수가 가장 높은 값을 출력
"""

"""
PriorityQueue
(현재까지의 총 점프 횟수가 적은 토끼, 현재 서있는 행 번호 + 열 번호가 작은 토끼, 행 번호가 작은 토끼, 열 번호가 작은 토끼, 고유번호가 작은 토끼)

토끼 class를 만들자

고유번호를 idx로 토끼를 찾을 수 있는 별도의 자료구조 (dict?)

점수는 따로 저장 (list?)

P + Q * (K * (logP + P + K)) + PlogP

P: 2000
Q: 4000
K: 100

"""

import heapq

CHECK = False

class Rabbit:
    def __init__(self, id, jump_range):
        self.id = id
        self.jump_range = jump_range
        self.total_jump = 0
        self.row = 0
        self.col = 0
        self.score = 0

num_cmd = int(input())

rabbit_dict = {}
rabbit_heap = []
rabbit_list = []

first_cmd = list(map(int, input().split()))
num_row, num_col, num_rabbit = first_cmd[1], first_cmd[2], first_cmd[3]
for rabbit_idx in range(num_rabbit):
    cur_rabbit_id = first_cmd[4+2*rabbit_idx]
    cur_rabbit_jump_range = first_cmd[4+2*rabbit_idx+1]
    cur_rabbit = Rabbit(cur_rabbit_id, cur_rabbit_jump_range)
    
    rabbit_dict[cur_rabbit_id] = cur_rabbit
    # 총 점프 횟수 / 행 + 열 / 행 / 열 / 고유번호
    heapq.heappush(rabbit_heap, (0, 0+0, 0, 0, cur_rabbit_id))
    rabbit_list.append(cur_rabbit)

def visualize():
    print_map = [["X"] * num_col for _ in range(num_row)]
    for rabbit in rabbit_list:
        if print_map[rabbit.row][rabbit.col] == "X":
            print_map[rabbit.row][rabbit.col] = f"{rabbit.id}"
        else:
            print_map[rabbit.row][rabbit.col] += f"/{rabbit.id}"
    for row in print_map:
        print("\t\t".join(map(str, row)))
    print()
    for rabbit in rabbit_list:
        print(f"ID: {rabbit.id} / jump range: {rabbit.jump_range} / total jump: {rabbit.total_jump} / score: {rabbit.score}")
    print()
    print()

if CHECK:
    visualize()

def play(num_round, plus_point):
    chosen_rabbit_list = []

    for round_idx in range(num_round):
        chosen_rabbit_id = heapq.heappop(rabbit_heap)
        chosen_rabbit_id = chosen_rabbit_id[-1]
        chosen_rabbit = rabbit_dict[chosen_rabbit_id]
        
        destination_heap = []
        
        # 위로 올라가는 경우
        if chosen_rabbit.jump_range <= chosen_rabbit.row:
            next_row = chosen_rabbit.row - chosen_rabbit.jump_range
        else:
            remain_range = chosen_rabbit.jump_range - chosen_rabbit.row
            next_dir = remain_range // (num_row - 1)
            if next_dir % 2 == 0:
                next_row = remain_range % (num_row - 1)
            else:
                next_row = (num_row - 1) - (remain_range % (num_row - 1))
        next_col = chosen_rabbit.col
        heapq.heappush(destination_heap, (-(next_row + next_col), -next_row, -next_col))

        # 아래로 내려가는 경우
        if chosen_rabbit.row + chosen_rabbit.jump_range <= num_row - 1:
            next_row = chosen_rabbit.row + chosen_rabbit.jump_range
        else:
            remain_range = chosen_rabbit.jump_range - (num_row - 1 - chosen_rabbit.row)
            next_dir = remain_range // (num_row - 1)
            if next_dir % 2 == 0:
                next_row = (num_row - 1) - (remain_range % (num_row - 1))
            else:
                next_row = remain_range % (num_row - 1)
        next_col = chosen_rabbit.col
        heapq.heappush(destination_heap, (-(next_row + next_col), -next_row, -next_col))
        
        # 오른쪽으로 가는 경우
        if chosen_rabbit.col + chosen_rabbit.jump_range <= num_col - 1:
            next_col = chosen_rabbit.col + chosen_rabbit.jump_range
        else:
            remain_range = chosen_rabbit.jump_range - (num_col - 1 - chosen_rabbit.col)
            next_dir = remain_range // (num_col - 1)
            if next_dir % 2 == 0:
                next_col = (num_col - 1) - (remain_range % (num_col - 1))
            else:
                next_col = remain_range % (num_col - 1)
        next_row = chosen_rabbit.row
        heapq.heappush(destination_heap, (-(next_row + next_col), -next_row, -next_col))

        # 왼쪽으로 가는 경우
        if chosen_rabbit.jump_range <= chosen_rabbit.col:
            next_col = chosen_rabbit.col - chosen_rabbit.jump_range
        else:
            remain_range = chosen_rabbit.jump_range - chosen_rabbit.col
            next_dir = remain_range // (num_col - 1)
            if next_dir % 2 == 0:
                next_col = remain_range % (num_col - 1)
            else:
                next_col = (num_col - 1) - (remain_range % (num_col - 1))
        next_row = chosen_rabbit.row
        heapq.heappush(destination_heap, (-(next_row + next_col), -next_row, -next_col))
        
        _, next_row, next_col = heapq.heappop(destination_heap)
        next_row = -next_row
        next_col = -next_col
        chosen_rabbit.row = next_row
        chosen_rabbit.col = next_col

        for rabbit in rabbit_list:
            if rabbit.id != chosen_rabbit.id:
                rabbit.score += (next_row + 1 + next_col + 1)
            else:
                rabbit.total_jump += 1
                # 총 점프 횟수 / 행 + 열 / 행 / 열 / 고유번호
                heapq.heappush(rabbit_heap, (rabbit.total_jump, (rabbit.row + rabbit.col), rabbit.row, rabbit.col, rabbit.id))
                if rabbit not in chosen_rabbit_list:
                    chosen_rabbit_list.append(rabbit)
        
    chosen_rabbit_list.sort(key=lambda x: (-(x.row+x.col), -x.row, -x.col))
    final_chosen_rabbit = chosen_rabbit_list[0]
    final_chosen_rabbit.score += plus_point
        
def range_up(rabbit_id, weight):
    cur_rabbit = rabbit_dict[rabbit_id]
    cur_rabbit.jump_range *= weight

for cmd_idx in range(num_cmd-1):
    cur_cmd = list(map(int, input().split()))
    if cur_cmd[0] == 200:
        play(cur_cmd[1], cur_cmd[2])
        if CHECK:
            print(f"Play for {cur_cmd[1]} rounds and add {cur_cmd[2]} points")
            visualize()

    elif cur_cmd[0] == 300:
        range_up(cur_cmd[1], cur_cmd[2])
        if CHECK:
            print(f"{cur_cmd[1]} rabbit X {cur_cmd[2]} range")
            visualize()

    elif cur_cmd[0] == 400:
        max_score = 0
        for rabbit in rabbit_list:
            max_score = max(max_score, rabbit.score)
        print(max_score)
        # if CHECK:
        #     print(f"choose the best rabbit")
        #     visualize()