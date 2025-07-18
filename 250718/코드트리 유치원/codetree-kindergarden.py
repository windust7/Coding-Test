"""
맨 처음에는 1번 학생을 줄을 세우고 그 뒤부터는 다음 세 행동을 반복하면서 줄을 세운다

1. a번 학생 뒤에 b명의 학생을 줄 세운다
2. a번 학생 앞에 b명의 학생을 줄 세운다
3. a번 학생 앞과 뒤에 있는 학생의 번호를 찾는다
"""

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
    
    def push_back(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            connect(self.head, new_node)
            self.tail = new_node
        else:
            connect(self.tail, new_node)
            self.tail = new_node
    
    def action_1(self, target_node, move_first_node, move_last_node):
        disconnect(move_first_node.prev, move_first_node)
        disconnect(move_last_node, move_last_node.next)
        if self.head is None:
            pass
        elif self.head == self.tail:
            connect(self.head, move_first_node)
            self.tail = move_last_node
        else:
            if target_node == self.tail:
                connect(self.tail, move_first_node)
                self.tail = move_last_node
            else:
                original_next_node = target_node.next
                disconnect(target_node, original_next_node)
                connect(target_node, move_first_node)
                connect(move_last_node, original_next_node)
    
    def action_2(self, target_node, move_first_node, move_last_node):
        disconnect(move_first_node.prev, move_first_node)
        disconnect(move_last_node, move_last_node.next)
        if self.head is None:
            pass
        elif self.head == self.tail:
            connect(move_last_node, self.head)
            self.head = move_first_node
        else:
            if target_node == self.head:
                connect(move_last_node, self.head)
                self.head = move_first_node
            else:
                original_prev_node = target_node.prev
                disconnect(original_prev_node, target_node)
                connect(original_prev_node, move_first_node)
                connect(move_last_node, target_node)
    
    def action_3(self, target_node):
        if target_node.prev is None or target_node.next is None:
            return -1
        else:
            return f"{target_node.prev.data} {target_node.next.data}"

original_dll = DoublyLinkedList()
result_dll = DoublyLinkedList()
node_dict = {}

first_node = Node(1)
node_dict[1] = first_node
result_dll.push_back(first_node)
for node_idx in range(2, 200000+1):
    cur_node = Node(node_idx)
    node_dict[node_idx] = cur_node
    original_dll.push_back(cur_node)

cur_turn = 2
for cmd_idx in range(num_cmd):
    cur_cmd = list(map(int, input().split()))
    if cur_cmd[0] == 1:
        result_dll.action_1(node_dict[cur_cmd[1]], node_dict[cur_turn], node_dict[cur_turn+cur_cmd[2]-1])
        cur_turn += cur_cmd[2]
    elif cur_cmd[0] == 2:
        result_dll.action_2(node_dict[cur_cmd[1]], node_dict[cur_turn], node_dict[cur_turn+cur_cmd[2]-1])
        cur_turn += cur_cmd[2]
    elif cur_cmd[0] == 3:
        print(result_dll.action_3(node_dict[cur_cmd[1]]))
    else:
        print(f"Wrong cmd: {cmd}")