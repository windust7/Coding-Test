"""
n x n 격자
무기 or 플레이어 or 빈 격자

총: 공격력
플레이어: 능력치, 플레이어 번호, 방향

1. 플레이어 이동
    1-1. range 밖이면 반대로 1만큼 이동
    1-2. 총이 있으면 획득. 내가 지금 들고 있는 것과 지금 구한 것 중에 더 쎈걸 두고 나머지는 해당 격자에 둔다
    1-3. 플레이어를 만나면 (능력치 + 총의 공격력) 비교해서 더 센놈이 이김. 같으면 초기 능력치가 높은 애가 이김. 
        1-3-1. 이기면 차이를 포인트로 획득. 
            1-3-1-1. 승리한 칸에 있는 총이랑 들고 있는 총 중에 제일 공격력이 높은 것만 가짐
        1-3-2. 지면 총을 두고 한칸 전진
            1-3-2-1. 다른 플레이어가 있거나 격자 범위 밖이면 오른쪽으로 90씩 회전하여 빈 칸이 보이는 순간 이동. 총은 같은 법칙으로 획득

"""

map_size, player_num, round_num = map(int, input().split())
gun_map_dict = {}
for row_idx in range(map_size):
    cur_row = list(map(int, input().split()))
    for col_idx in range(map_size):
        gun_map_dict[(row_idx, col_idx)] = [cur_row[col_idx]]

class Player():
    def __init__(self, row_idx, col_idx, direction, status, idx):
        self.row = row_idx
        self.col = col_idx
        self.direction = direction
        self.status = status
        self.gun = 0
        self.idx = idx

    def get_power(self):
        return self.status + self.gun

    def move(self):
        next_row = self.row + dx[self.direction]
        next_col = self.col + dy[self.direction]
        if not (0 <= next_row < map_size and 0 <= next_col < map_size):
            self.direction = (self.direction + 2) % 4
            next_row = self.row + dx[self.direction]
            next_col = self.col + dy[self.direction]

        player_coord_dict.pop((self.row, self.col))
        self.row, self.col = next_row, next_col

        if (self.row, self.col) not in player_coord_dict.keys():
            player_coord_dict[(self.row, self.col)] = self.idx
            if len(gun_map_dict[(self.row, self.col)]) == 1 and gun_map_dict[(self.row, self.col)][0] == 0:
                pass
            else:
                cur_gun_list = gun_map_dict[(self.row, self.col)][:]
                cur_gun_list.append(self.gun)
                cur_gun_list.sort()
                self.gun = cur_gun_list.pop()
                if cur_gun_list[-1] == 0:
                    cur_gun_list = [0]
                gun_map_dict[(self.row, self.col)] = cur_gun_list
        else:
            other_player_idx = player_coord_dict[(self.row, self.col)]
            other_player = player_list[other_player_idx]
            if self.get_power() > other_player.get_power():
                result_list[self.idx] += (self.get_power() - other_player.get_power())
                player_coord_dict.pop((other_player.row, other_player.col))
                player_coord_dict[(self.row, self.col)] = self.idx
                other_player.lose_move()
                self.win_move()
            elif self.get_power() == other_player.get_power():
                if self.status > other_player.status:
                    player_coord_dict.pop((other_player.row, other_player.col))
                    player_coord_dict[(self.row, self.col)] = self.idx
                    other_player.lose_move()
                    self.win_move()
                else:
                    self.lose_move()
                    other_player.win_move()
            elif self.get_power() < other_player.get_power():
                result_list[other_player_idx] += -(self.get_power() - other_player.get_power())
                self.lose_move()
                other_player.win_move()

    def win_move(self):
        if not (len(gun_map_dict[(self.row, self.col)]) == 1 and gun_map_dict[(self.row, self.col)][0] == 0):
            cur_gun_list = gun_map_dict[(self.row, self.col)][:]
            cur_gun_list.append(self.gun)
            cur_gun_list.sort()
            self.gun = cur_gun_list.pop()
            if cur_gun_list[-1] == 0:
                cur_gun_list = [0]
            gun_map_dict[(self.row, self.col)] = cur_gun_list

    def lose_move(self):
        if self.gun != 0:
            gun_map_dict[(self.row, self.col)].append(self.gun)
            gun_map_dict[(self.row, self.col)].sort()
            self.gun = 0
        next_row = self.row + dx[self.direction]
        next_col = self.col + dy[self.direction]
        while not ((0 <= next_row < map_size and 0 <= next_col < map_size) and (next_row, next_col) not in player_coord_dict.keys()):
            self.direction = (self.direction + 1) % 4
            next_row = self.row + dx[self.direction]
            next_col = self.col + dy[self.direction]

        # player_coord_dict.pop((self.row, self.col))
        self.row, self.col = next_row, next_col
        player_coord_dict[(self.row, self.col)] = self.idx

        if len(gun_map_dict[(self.row, self.col)]) == 1 and gun_map_dict[(self.row, self.col)][0] == 0:
            pass
        else:
            cur_gun_list = gun_map_dict[(self.row, self.col)][:]
            cur_gun_list.append(self.gun)
            cur_gun_list.sort()
            self.gun = cur_gun_list.pop()
            if cur_gun_list[-1] == 0:
                cur_gun_list = [0]
            gun_map_dict[(self.row, self.col)] = cur_gun_list

    def __str__(self):
        dir_dict = {0: "^", 1: ">", 2: "v", 3: "<"}
        return f"idx: {self.idx} / coord: {self.row}, {self.col} / power: {self.status} + {self.gun} / dir: {dir_dict[self.direction]}"


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

player_list = []
player_coord_dict = {}
for player_idx in range(player_num):
    cur_row, cur_col, cur_dir, cur_status = map(int, input().split())
    player_list.append(Player(cur_row-1, cur_col-1, cur_dir, cur_status, player_idx))
    player_coord_dict[(cur_row-1, cur_col-1)] = player_idx

def visualize():
    for row_idx in range(map_size):
        for col_idx in range(map_size):
            print("/".join(map(str, gun_map_dict[(row_idx, col_idx)])), end="")
            print("\t", end="")
        print()
    print()
    for player in player_list:
        print(player)
    print()
    for player_coord in player_coord_dict:
        print(f"{player_coord}: {player_coord_dict[player_coord]}")
    print()
    print(" ".join(map(str, result_list)))
    print()
    print(f"==========")
    print()

result_list = [0] * player_num

for round_idx in range(round_num):
    # visualize()
    for player in player_list:
        player.move()

print(" ".join(map(str, result_list)))