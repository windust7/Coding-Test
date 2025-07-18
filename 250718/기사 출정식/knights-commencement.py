"""
원탁에 N명의 기사, 번호가 하나씩 있음
왕이 기사의 번호를 부르면, 그 기사가 일어남
    일어나면서 자신의 왼쪽과 오른쪽에 있는 기사들의 번호를 외치고 없어짐
    총 M번 부름
"""

CHECK = False

num_people, num_cmd = map(int, input().split())


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
        self.num_node = 0

    def push_back(self, new_node):
        if self.num_node == 0:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        elif self.num_node == 1:
            connect(self.head, new_node)
            connect(new_node, self.head)
        else:
            cur_tail = self.head.prev
            disconnect(cur_tail, self.head)
            connect(cur_tail, new_node)
            connect(new_node, self.head)
        self.num_node += 1

    def pop(self, pop_node):
        if self.num_node == 0:
            pass
        elif self.num_node == 1:
            pass
        elif self.num_node == 2:
            pass
        else:
            if pop_node == self.head:
                next_head = self.head.next
                original_tail = self.head.prev
                disconnect(original_tail, self.head)
                disconnect(self.head, next_head)
                connect(original_tail, next_head)
                self.head = next_head
                print(f"{self.head.data} {original_tail.data}")
                self.num_node -= 1
            else:
                left_node = pop_node.next
                right_node = pop_node.prev
                disconnect(right_node, pop_node)
                disconnect(pop_node, left_node)
                connect(right_node, left_node)
                print(f"{left_node.data} {right_node.data}")
                self.num_node -= 1

    def __str__(self):
        if self.num_node == 0:
            return "EMPTY"
        else:
            return_str = f"total: {self.num_node}\n"
            cur_node = self.head
            while True:
                return_str += str(cur_node) + "\n"
                cur_node = cur_node.next
                if cur_node == self.head:
                    break
            return_str += "\n"
            return return_str


cll = CirclyLinkedList()
node_dict = {}
people_list = list(map(int, input().split()))

for person in people_list:
    cur_node = Node(person)
    node_dict[person] = cur_node
    cll.push_back(cur_node)

for cmd_idx in range(num_cmd):
    if CHECK:
        print()
        print(cll)
    cur_cmd = int(input())
    cur_node = node_dict[cur_cmd]
    cll.pop(cur_node)