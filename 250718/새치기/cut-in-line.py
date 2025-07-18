"""
N명의 사람들이 M개의 줄에 나눠서 줄을 서고 있다

1 a b:      a번의 사람이 b인 사람 앞으로 새치기 했다
2 a:        a번의 사람이 없어졌다
3 a b c:    a번부터 b번까지 c번 앞으로 새치기 했다 (순서 유지)
"""

CHECK = False

num_people, num_queue, num_cmd = map(int, input().split())

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

    def action_1(self, node_b, node_a):
        disconnect(node_b.prev, node_b)
        disconnect(node_b, node_b.next)
        if self.head is None:
            pass
        elif self.head == self.tail:
            connect(node_b, node_a)
            self.head = node_b
        else:
            if node_a == self.head:
                connect(node_b, node_a)
                self.head = node_b
            else:
                original_prev = node_a.prev
                disconnect(original_prev, node_a)
                connect(original_prev, node_b)
                connect(node_b, node_a)

    def action_2(self, node_a):
        if self.head is None:
            pass
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if node_a == self.head:
                next_head = node_a.next
                disconnect(node_a, next_head)
                self.head = next_head
            elif node_a == self.tail:
                next_tail = node_a.prev
                disconnect(next_tail, node_a)
                self.tail = next_tail
            else:
                original_prev = node_a.prev
                original_next = node_a.next
                disconnect(original_prev, node_a)
                disconnect(node_a, original_next)
                connect(original_prev, original_next)

    def action_3(self, node_b, node_c, node_a):
        disconnect(node_b.prev, node_b)
        disconnect(node_c, node_c.next)
        if self.head is None:
            pass
        elif self.head == self.tail:
            connect(node_c, self.head)
            self.head = node_b
        else:
            if node_a == self.head:
                connect(node_c, node_a)
                self.head = node_b
            else:
                original_prev = node_a.prev
                disconnect(original_prev, node_a)
                connect(original_prev, node_b)
                connect(node_c, node_a)

    def pop(self, pop_node):
        if pop_node == self.head:
            if pop_node == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = pop_node.next
                disconnect(pop_node, pop_node.next)
        elif pop_node == self.tail:
            self.tail = pop_node.prev
            disconnect(pop_node.prev, pop_node)
        else:
            pop_node_prev = pop_node.prev
            pop_node_next = pop_node.next
            disconnect(pop_node_prev, pop_node)
            disconnect(pop_node, pop_node_next)
            connect(pop_node.prev, pop_node_next)

    def result_print(self):
        if self.head is None:
            print(-1)
        else:
            return_str = ""
            cur_node = self.head
            while True:
                return_str += f"{cur_node.data} "
                if cur_node == self.tail:
                    break
                else:
                    cur_node = cur_node.next
            print(return_str)

queue_list = [DoublyLinkedList() for _ in range(num_queue)]
node_dict = {}
node_queue_dict = {}

for queue_idx in range(num_queue):
    cur_queue = list(map(int, input().split()))
    for data in cur_queue[1:]:
        new_node = Node(data)
        node_dict[data] = new_node
        node_queue_dict[data] = queue_idx
        queue_list[queue_idx].push_back(new_node)

for cmd_idx in range(num_cmd):
    cur_cmd = list(map(int, input().split()))
    if cur_cmd[0] == 1:
        if CHECK:
            print(f"{cur_cmd[1]} -> {cur_cmd[2]}")
        node_a = node_dict[cur_cmd[1]]
        node_a_queue = queue_list[node_queue_dict[cur_cmd[1]]]
        node_a_queue.pop(node_a)
        node_b = node_dict[cur_cmd[2]]
        node_b_queue = queue_list[node_queue_dict[cur_cmd[2]]]
        node_b_queue.action_1(node_a, node_b)
        node_queue_dict[cur_cmd[1]] = node_queue_dict[cur_cmd[2]]
    elif cur_cmd[0] == 2:
        if CHECK:
            print(f"{cur_cmd[1]} -> OUT")
        node_a = node_dict[cur_cmd[1]]
        node_a_queue = queue_list[node_queue_dict[cur_cmd[1]]]
        node_a_queue.action_2(node_a)
    elif cur_cmd[0] == 3:
        if CHECK:
            print(f"{cur_cmd[1]} ~ {cur_cmd[2]} -> {cur_cmd[3]}")
        node_a = node_dict[cur_cmd[1]]
        node_b = node_dict[cur_cmd[2]]
        node_c = node_dict[cur_cmd[3]]

        node_a_queue = queue_list[node_queue_dict[cur_cmd[1]]]
        node_c_queue = queue_list[node_queue_dict[cur_cmd[3]]]

        if node_a == node_a_queue.head:
            if node_a == node_a_queue.tail:
                node_a_queue.head = None
                node_a_queue.tail = None
            else:
                node_a_queue.head = node_b.next
        if node_b == node_a_queue.tail:
            node_a_queue.tail = node_a.prev

        cur_node = node_a

        while True:
            node_queue_dict[cur_node.data] = node_queue_dict[cur_cmd[3]]
            if cur_node == node_b:
                break
            else:
                cur_node = cur_node.next
        node_c_queue.action_3(node_a, node_b, node_c)
    else:
        print(f"Wrong cmd: {cur_cmd}")

    if CHECK:
        print()
        for queue in queue_list:
            queue.result_print()
        print()
        
for queue in queue_list:
    queue.result_print()