"""
순서대로 q개의 명령 수행

1. 공장 설립
    m개의 벨트 설치
    각각 n / m 개의 물건
    물건: id랑 weight
    O(n*m) + O(n*m)
        dictionary에 key: id / value: 그 node

2. 물건 하차
    상자의 최대 무게 w_max
    1번부터 m번까지 순서대로 벨트를 보며 맨 앞에 있는 선물이 w_max 이하면 하차. 하차해도 벨트 끝까지 진행
        하차한다면 남은 것들은 한 칸씩 앞으로
        아니면 벨트 맨 뒤로
        return 상자 무게의 총 합
    O(m) + O(1)

3. 물건 제거
    제거할 물건 r_id
    해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면, 그 벨트에서 상자를 제거하고 나머지들은 한 칸씩 앞으로
    return r_id or -1 (없으면)
    O(1) + O(m)
        먼저 dictionary로 있는지 보고

4. 물건 확인
    확인할 번호 f_id
    해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있으면 해당 "벨트"의 번호를 출력, 없으면 -1
    있으면 해당 상자와 그 뒤에 있는 모든 상자를 전부 맨 앞으로 가져온다 (순서 유지)
    O(1) + O(m)
        먼저 dictionary로 있는지 보고

5. 벨트 고장
    고장이 발생한 번호 b_num
    해당 벨트의 바로 오른쪽 벨트부터 순서대로 보면서 아직 고장이 나지 않은 최초의 벨트 위로 앞에서부터 순서대로 하나씩 옮긴다
    끝까지 가면 다시 1번 벨트로
    return -1 (이미 망가져 있음) or b_num (정상적으로 고장 처리)
    O(m) + O(1)
"""


# Doubly Linked List
class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.next = None
        self.prev = None

    def __str__(self):
        return f"id: {self.id} / weight: {self.weight}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
        self.is_broken = False

    def push_front(self, new_id, new_weight):
        new_node = Node(new_id, new_weight)
        new_node.next = self.head
        new_node.prev = None

        if self.head != None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

        self.node_num += 1

    def push_back(self, new_id, new_weight, belt_idx):
        new_node = Node(new_id, new_weight)
        new_node.prev = self.tail
        new_node.next = None

        if self.tail != None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

        self.node_num += 1

        belt_dict_list[belt_idx][new_id] = new_node

    def pop_front(self):
        if self.head == None:
            return None
        elif self.node_num == 1:
            tmp = self.head
            self.head = None
            self.tail = None
            self.node_num -= 1
            return tmp.id, tmp.weight
        else:
            tmp = self.head
            self.head = tmp.next
            self.head.prev = None
            tmp.next = None
            self.node_num -= 1
            return tmp.id, tmp.weight

    def pop_back(self):
        if self.tail == None:
            return None
        elif self.node_num == 1:
            tmp = self.tail
            self.tail = None
            self.head = None
            self.node_num -= 1
            return tmp.id, tmp.weight
        else:
            tmp = self.tail
            self.tail = tmp.prev
            self.tail.next = None
            tmp.prev = None
            self.node_num -= 1
            return tmp.id, tmp.weight

    def front(self):
        if self.head == None:
            return None
        else:
            return self.head.id, self.head.weight

    def back(self):
        if self.tail == None:
            return None
        else:
            return self.tail.id, self.tail.weight

    def __str__(self):
        return_str = f"total: {self.node_num}\n"
        if self.head is not None and not self.is_broken:
            cur_node = self.head
            while True:
                return_str += f"{cur_node.id} / {cur_node.weight}\n"
                if cur_node == self.tail:
                    break
                cur_node = cur_node.next
        if self.is_broken:
            return_str += "BROKEN\n"
        return_str += f"\n"
        return return_str


def pick_box(w_max):
    result_list = []
    for belt_idx, belt in enumerate(belt_list):
        if belt.is_broken:
            continue
        if belt.head is None:
            continue
        if belt.head.weight <= w_max:
            cur_id, cur_weight = belt.pop_front()
            result_list.append(cur_weight)
            belt_dict_list[belt_idx].pop(cur_id)
        else:
            cur_id, cur_weight = belt.pop_front()
            belt.push_back(cur_id, cur_weight, belt_idx)
    return sum(result_list)


def remove_box(r_id):
    for belt_idx, belt_dict in enumerate(belt_dict_list):
        if belt_list[belt_idx].is_broken:
            continue
        if r_id in belt_dict.keys():
            cur_node = belt_dict.pop(r_id)
            belt_list[belt_idx].node_num -= 1
            if cur_node.prev is None:
                belt_list[belt_idx].pop_front()
            elif cur_node.next is None:
                belt_list[belt_idx].pop_back()
            else:
                cur_node.prev.next = cur_node.next
                cur_node.next.prev = cur_node.prev
                cur_node.prev, cur_node.next = None, None
            return r_id
    return -1


def check_box(f_id):
    for belt_idx, belt_dict in enumerate(belt_dict_list):
        if belt_list[belt_idx].is_broken:
            continue
        if f_id in belt_dict.keys():
            cur_belt = belt_list[belt_idx]
            cur_node = belt_dict[f_id]
            prev_head, prev_tail = cur_belt.head, cur_belt.tail
            if cur_node.prev is None:
                return belt_idx + 1
            else:
                cur_belt.head, cur_belt.tail = cur_node, cur_node.prev
                cur_node.prev = None
                cur_belt.tail.next = None
                prev_head.prev = prev_tail
                prev_tail.next = prev_head
                return belt_idx + 1
    return -1


def broken_belt(b_num):
    broken_belt_idx = b_num - 1
    broken_belt = belt_list[broken_belt_idx]
    broken_belt_dict = belt_dict_list[broken_belt_idx]
    if not broken_belt.is_broken:
        broken_belt.is_broken = True
        while True:
            broken_belt_idx = (broken_belt_idx + 1) % len(belt_list)
            if not belt_list[broken_belt_idx].is_broken:
                break
        move_belt = belt_list[broken_belt_idx]
        move_belt.tail.next = broken_belt.head
        broken_belt.head.prev = move_belt.tail
        move_belt.tail = broken_belt.tail
        move_belt.node_num += broken_belt.node_num
        move_belt_dict = belt_dict_list[broken_belt_idx]
        for _key in broken_belt_dict.keys():
            move_belt_dict[_key] = broken_belt_dict[_key]
        return b_num
    else:
        return -1


def visualize():
    for belt in belt_list:
        print(belt)
    print()
    for belt_dict in belt_dict_list:
        for belt_dict_key in belt_dict.keys():
            print(f"{belt_dict[belt_dict_key]}\t|||\t", end=" ")
        print()
    print()
    print()
    print()


command_num = int(input())

commands = []
for command_idx in range(command_num):
    cur_command = list(map(int, input().split()))
    commands.append(cur_command)

for cmd_idx, cmd in enumerate(commands):
    if cmd_idx == 0:
        box_num, belt_num = cmd[1], cmd[2]
        belt_list = [DoublyLinkedList() for _ in range(belt_num)]
        belt_dict_list = [{} for _ in range(belt_num)]
        for box_idx in range(box_num):
            belt_idx = box_idx // (box_num // belt_num)
            cur_belt = belt_list[belt_idx]
            cur_belt.push_back(cmd[3 + box_idx], cmd[3 + box_idx + box_num], belt_idx)
        # visualize()
        # break
    else:
        if cmd[0] == 200:
            print(pick_box(cmd[1]))
            # print(f"pick box: {cmd[1]}")
            # visualize()
        elif cmd[0] == 300:
            print(remove_box(cmd[1]))
            # print(f"remove box:{cmd[1]}")
            # visualize()
        elif cmd[0] == 400:
            print(check_box(cmd[1]))
            # print(f"check box: {cmd[1]}")
            # visualize()
        elif cmd[0] == 500:
            print(broken_belt(cmd[1]))
            # print(f"broken belt: {cmd[1]}")
            # visualize()
        else:
            print(f"Wrong command in {cmd_idx}: {cmd}")