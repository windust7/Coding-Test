"""
1. A 학생과 B 학생이 속한 원을 잇기
2. A 학생부터 시작해서 시계방향으로 돌면서 B 학생 전까지 원을 새로 만들기
3. A 학생이 속한 원 안에서 학생 번호가 가장 작은 학생부터 반시계 방향으로 자신의 번호 외치기
    3-1. 이건 제일 마지막에만 주어진다
"""

"""
cll: 어짜피 그냥 head만 알고 있으면 된다
1: 새로운 cll 객체 생성
2: 새로운 cll 객체 2개 생성
3: 한바퀴 돌면서 min찾고, 그 min부터 출력
"""

num_node, num_circle, num_cmd = map(int, input().split())

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

class CirclyLinkedList:
    def __init__(self):
        self.head = None
    
    def push_back(self, new_node):
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        elif self.head.next == self.head:
            connect(self.head, new_node)
            connect(new_node, self.head)
        else:
            original_tail = self.head.prev
            disconnect(original_tail, self.head)
            connect(original_tail, new_node)
            connect(new_node, self.head)
    
node_dict = {}
circle_list = [CirclyLinkedList() for _ in range(num_circle)]
for circle_idx in range(num_circle):
    cur_circle = list(map(int, input().split()))
    for data in cur_circle[1:]:
        cur_node = Node(data)
        circle_list[circle_idx].push_back(cur_node)
        node_dict[data] = cur_node

for cmd_idx in range(num_cmd):
    cur_cmd = list(map(int, input().split()))
    if cur_cmd[0] == 1:
        node_a = node_dict[cur_cmd[1]]
        node_b = node_dict[cur_cmd[2]]

        if node_a == node_a.prev:
            if node_b == node_b.prev:
                connect(node_a, node_b)
                connect(node_b, node_a)
            else:
                original_b_prev = node_b.prev
                disconnect(original_b_prev, node_b)
                connect(node_a, node_b)
                connect(original_b_prev, node_a)
        else:
            if node_b == node_b.prev:
                original_a_next = node_a.next
                disconnect(node_a, original_a_next)
                connect(node_a, node_b)
                connect(node_b, original_a_next)
            else:
                original_a_next = node_a.next
                original_b_prev = node_b.prev
                disconnect(node_a, original_a_next)
                disconnect(original_b_prev, node_b)
                connect(node_a, node_b)
                connect(original_b_prev, original_a_next)


    elif cur_cmd[0] == 2:
        node_a = node_dict[cur_cmd[1]]
        node_b = node_dict[cur_cmd[2]]

        if node_a == node_a.prev:
            if node_b == node_b.prev:
                pass
            else:
                pass
        else:
            if node_b == node_b.prev:
                pass
            else:
                if node_a.prev == node_b:
                    original_b_prev = node_b.prev
                    disconnect(original_b_prev, node_b)
                    disconnect(node_b, node_a)
                    connect(original_b_prev, node_a)
                    node_b.next = node_b
                    node_b.prev = node_b
                elif node_a.next == node_b:
                    original_a_prev = node_a.prev
                    disconnect(original_a_prev, node_a)
                    disconnect(node_a, node_b)
                    connect(original_a_prev, node_b)
                    node_a.next = node_a
                    node_a.prev = node_a
                else:
                    original_a_prev = node_a.prev
                    original_b_prev = node_b.prev
                    disconnect(original_b_prev, node_b)
                    disconnect(original_a_prev, node_a)
                    connect(original_b_prev, node_a)
                    connect(original_a_prev, node_b)

    elif cur_cmd[0] == 3:
        node = node_dict[cur_cmd[1]]
        
        min_data = node.data
        min_node = node
        cur_node = node
        while True:
            if min_data > cur_node.data:
                min_node = cur_node
                min_data = cur_node.data
            cur_node = cur_node.prev
            if cur_node == node:
                break
        cur_node = min_node
        while True:
            print(f"{cur_node.data}", end=" ")
            cur_node = cur_node.prev
            if cur_node == min_node:
                break



    else:
        print(f"Wrong cmd: {cur_cmd}")