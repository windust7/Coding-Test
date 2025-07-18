"""
1. n개의 벨트, m개의 물건
    1-1. 물건은 오름차순으로 올라감

2. m_src번째의 벨트에 있는 모든 물건을 m_dst번째의 벨트 제일 앞으로 옮김
    2-1. m_src번째 벨트에 물건이 없다면 무시
    2-2. 옮기고 나서 m_dst의 물건 개수를 출력

3. m_src번째의 벨트의 가장 앞에 있는 물건을 m_dst번째의 벨트의 가장 앞에 있는 물건과 교체
    3-1. 둘 중에 하나라도 물건이 없으면 옮기기만 함
    3-2. 옮기고 나서 m_dst번째 벨트의 물건 개수를 출력

4. m_src번째의 벨트에 있는 물건 개수 // 2 번째까지 있는 물건을 m_dst 번째 벨트 앞으로 옮김.
    4-1. 최대 100번 -> 최대 100,000 X 100 = 10,000,000

5. 물건의 번호가 주어질 때, (앞 물건의 번호 + 뒷 물건의 번호 * 2)를 출력
    5-1. 만약에 앞 물건이 없으면 그 번호는 -1로 대체
    5-2. 만약에 뒷 물건이 없으면 그 번호는 -1로 대체

6. 벨트 번호가 주어질 때, (그 벨트의 제일 앞에 있는 물건의 번호 + 2 * 그 벨트의 제일 뒤에 있는 물건의 번호 + 3 * 그 벨트의 물건의 개수) 출력
    6-1. 물건이 없으면 -1로 대체
"""

CHECK = False

num_cmd = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    def __str__(self):
        return f"{self.data}"

def connect(front_node, back_node):
    if front_node is not None:
        front_node.next = back_node
    if back_node is not None:
        back_node.prev = front_node

def disconnect(front_node, back_node):
    if front_node is not None:
        front_node.next = None
    if back_node is not None:
        back_node.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_node = 0

    def push_front(self, new_node):
        if self.num_node == 0:
            self.head = new_node
            self.tail = new_node
        elif self.num_node == 1:
            connect(new_node, self.tail)
            self.head = new_node
        else:
            connect(new_node, self.head)
            self.head = new_node
        self.num_node += 1

    def push_back(self, new_node):
        if self.num_node == 0:
            self.head = new_node
            self.tail = new_node
        elif self.num_node == 1:
            connect(self.head, new_node)
            self.tail = new_node
        else:
            connect(self.tail, new_node)
            self.tail = new_node
        self.num_node += 1

    def pop_front(self):
        if self.num_node == 0:
            return None
        elif self.num_node == 1:
            return_node = self.head
            self.head = None
            self.tail = None
            self.num_node = 0
            return return_node
        else:
            return_node = self.head
            self.head = return_node.next
            disconnect(return_node, self.head)
            self.num_node -= 1
            return return_node

    def __str__(self):
        if self.num_node == 0:
            return "EMPTY\n"
        else:
            return_str = f"total: {self.num_node}\n"
            cur_node = self.head
            while True:
                return_str += f"{cur_node.data} "
                if cur_node == self.tail:
                    if cur_node.next is not None:
                        print(f"****************************** {cur_node} -> {cur_node.next} ******************************")
                    break
                else:
                    cur_node = cur_node.next
            return_str += "\n"
            return return_str

def visualize():
    for idx, belt in enumerate(belt_list[1:]):
        print(f"belt {idx + 1}:")
        print(belt)

first_cmd = list(map(int, input().split()))
assert first_cmd[0] == 100
num_belt, num_gift = first_cmd[1], first_cmd[2]
belt_list = [DoublyLinkedList() for _ in range(num_belt+1)]
gift_dict = {}
for item_idx, belt_idx in enumerate(first_cmd[3:]):
    new_gift = Node(item_idx+1)
    belt_list[belt_idx].push_back(new_gift)
    gift_dict[item_idx+1] = new_gift

if CHECK:
    visualize()

def action_2(cmd_list):
    m_src = cmd_list[1]
    m_dst = cmd_list[2]

    src_belt = belt_list[m_src]
    dst_belt = belt_list[m_dst]

    if src_belt.num_node == 0:
        pass
    elif src_belt.num_node == 1:
        move_gift = src_belt.head
        src_belt.head = None
        src_belt.tail = None
        src_belt.num_node = 0
        dst_belt.push_front(move_gift)
    else:
        move_start = src_belt.head
        move_end = src_belt.tail
        src_belt.head = None
        src_belt.tail = None

        connect(move_end, dst_belt.head)
        dst_belt.head = move_start

        dst_belt.num_node += src_belt.num_node
        src_belt.num_node = 0
    print(dst_belt.num_node)

def action_3(cmd_list):
    m_src = cmd_list[1]
    m_dst = cmd_list[2]

    src_belt = belt_list[m_src]
    dst_belt = belt_list[m_dst]

    if src_belt.num_node == 0:
        if dst_belt.num_node == 0:
            pass
        elif dst_belt.num_node == 1:
            from_dst = dst_belt.pop_front()
            src_belt.push_front(from_dst)
        else:
            from_dst = dst_belt.pop_front()
            src_belt.push_front(from_dst)
    elif src_belt.num_node == 1:
        if dst_belt.num_node == 0:
            from_src = src_belt.pop_front()
            dst_belt.push_front(from_src)
        elif dst_belt.num_node == 1:
            from_src = src_belt.pop_front()
            from_dst = dst_belt.pop_front()
            dst_belt.push_front(from_src)
            src_belt.push_front(from_dst)
        else:
            from_src = src_belt.pop_front()
            from_dst = dst_belt.pop_front()
            dst_belt.push_front(from_src)
            src_belt.push_front(from_dst)
    else:
        if dst_belt.num_node == 0:
            from_src = src_belt.pop_front()
            dst_belt.push_front(from_src)
        elif dst_belt.num_node == 1:
            from_src = src_belt.pop_front()
            from_dst = dst_belt.pop_front()
            dst_belt.push_front(from_src)
            src_belt.push_front(from_dst)
        else:
            from_src = src_belt.pop_front()
            from_dst = dst_belt.pop_front()
            dst_belt.push_front(from_src)
            src_belt.push_front(from_dst)
    print(dst_belt.num_node)

def action_4(cmd_list):
    m_src = cmd_list[1]
    m_dst = cmd_list[2]

    src_belt = belt_list[m_src]
    dst_belt = belt_list[m_dst]

    if src_belt.num_node == 0 or src_belt.num_node == 1:
        pass
    else:
        num_move = src_belt.num_node // 2
        move_start_gift = src_belt.head
        move_end_gift = src_belt.head
        for _ in range(num_move-1):
            move_end_gift = move_end_gift.next

        if move_start_gift == move_end_gift:
            src_belt.head = move_start_gift.next
            disconnect(move_start_gift, src_belt.head)
            if dst_belt.num_node == 0:
                dst_belt.head = move_start_gift
                dst_belt.tail = move_start_gift
            elif dst_belt.num_node == 1:
                connect(move_end_gift, dst_belt.head)
                dst_belt.head = move_start_gift
            else:
                connect(move_end_gift, dst_belt.head)
                dst_belt.head = move_start_gift
        else:
            src_belt.head = move_end_gift.next
            disconnect(move_end_gift, src_belt.head)
            if dst_belt.num_node == 0:
                dst_belt.head = move_start_gift
                dst_belt.tail = move_end_gift
            elif dst_belt_num_node == 1:
                conect(move_end_gift, dst_belt.head)
                dst_belt.head = move_start_gift
            else:
                conect(move_end_gift, dst_belt.head)
                dst_belt.head = move_start_gift

        src_belt.num_node -= num_move
        dst_belt.num_node += num_move

    print(dst_belt.num_node)

def action_5(cmd_list):
    p_num = cmd_list[1]
    target_gift = gift_dict[p_num]

    if target_gift.prev is None:
        a = -1
    else:
        a = target_gift.prev.data

    if target_gift.next is None:
        b = -1
    else:
        b = target_gift.next.data

    print(a + 2 * b)

def action_6(cmd_list):
    b_num = cmd_list[1]
    target_belt = belt_list[b_num]
    if target_belt.num_node == 0:
        a, b = -1, -1
    else:
        a = target_belt.head.data
        b = target_belt.tail.data
    c = target_belt.num_node
    print(a + 2 * b + 3 * c)

for cmd_idx in range(num_cmd-1):
    cur_cmd = list(map(int, input().split()))

    if cur_cmd[0] == 200:
        action_2(cur_cmd)
        if CHECK:
            print("==========")
            print(f"belt {cur_cmd[1]} 전부 belt {cur_cmd[2]} 앞으로")
            visualize()
    elif cur_cmd[0] == 300:
        action_3(cur_cmd)
        if CHECK:
            print("==========")
            print(f"belt {cur_cmd[1]} 제일 앞이랑 belt {cur_cmd[2]} 제일 앞이랑 교환")
            visualize()
    elif cur_cmd[0] == 400:
        action_4(cur_cmd)
        if CHECK:
            print("==========")
            print(f"belt {cur_cmd[1]}의 앞에서 반개까지 belt {cur_cmd[2]} 제일 앞으로")
            visualize()
    elif cur_cmd[0] == 500:
        action_5(cur_cmd)
        if CHECK:
            print("==========")
            print(f"{cur_cmd[1]}의 선물의 앞은 a, 뒤는 b라고 할 때 a + 2 * b")
            visualize()
    elif cur_cmd[0] == 600:
        action_6(cur_cmd)
        if CHECK:
            print("==========")
            print(f"{cur_cmd[1]} 벨트의 제일 앞은 a, 뒤를 b, 선물의 개수를 c라고 할 때 a + 2 * b + 3 * c")
            visualize()
    else:
        print(f"Wrong cmd: {cur_cmd}")