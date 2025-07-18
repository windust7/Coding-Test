"""
가고 싶은 N개의 도시에 스티커
최우선적으로 방문하고 싶은 도시에 핀셋

1. 핀셋을 꽂은 도시를 현재의 오른쪽 인접 도시로 바꿔서 꽂음.
    1-1. 오른쪽에 있는 도시가 없으면 무시

2. 핀셋을 꽂은 도시를 현재의 왼쪽 인접 도시로 바꿔서 꽂음.
    2-1. 왼쪽에 있는 도시가 없으면 무시

3. 핀셋을 꽂은 도시의 오른쪽에 있는 도시의 스티커를 제거
    3-1. 오른쪽에 도시가 없으면 무시

4. 핀셋을 꽂은 도시의 오른쪽에 새로운 도시를 추가해서 스티커를 붙임
"""

CHECK = False

num_city, num_cmd = map(int, input().split())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.tail = None
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

    def push_back(self, data):
        new_node = Node(data)
        if self.num_node == 0:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            self.num_node += 1
        elif self.num_node == 1:
            connect(self.head, new_node)
            connect(new_node, self.head)
            self.num_node += 1
        else:
            original_tail = self.head.prev
            disconnect(original_tail, self.head)
            connect(original_tail, new_node)
            connect(new_node, self.head)
            self.num_node += 1

    def push(self, data):
        new_node = Node(data)
        if self.num_node == 0:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            self.num_node += 1
        elif self.num_node == 1:
            connect(self.head, new_node)
            connect(new_node, self.head)
            self.num_node += 1
        else:
            # self.num_node == 2일 때는?
            original_next_node = self.head.next
            disconnect(self.head, original_next_node)
            connect(self.head, new_node)
            connect(new_node, original_next_node)
            self.num_node += 1
    
    def move_head_front(self):
        if self.num_node == 0:
            pass
        elif self.num_node == 1:
            pass
        else:
            self.head = self.head.next
    
    def move_head_back(self):
        if self.num_node == 0:
            pass
        elif self.num_node == 1:
            pass
        else:
            self.head = self.head.prev

    def remove(self):
        if self.num_node == 0:
            pass
        elif self.num_node == 1:
            pass
        elif self.num_node == 2:
            disconnect(self.head, self.head.next)
            self.head.next = self.head
            self.head.prev = self.head
            self.num_node -= 1
        else:
            original_next_node = self.head.next
            next_next_node = self.head.next.next
            disconnect(self.head, original_next_node)
            disconnect(original_next_node, next_next_node)
            connect(self.head, next_next_node)
            self.num_node -= 1
    
    def __str__(self):
        if self.num_node == 0:
            return "EMPTY"
        else:
            return_str = f"total: {self.num_node}"
            cur_node = self.head
            while True:
                return_str += str(cur_node)
                cur_node = cur_node.next
                if cur_node == self.head:
                    break
            return_str += "\n"
            return return_str

    def result_print(self):
        if self.num_node == 0:
            print(-1)
        elif self.num_node == 1:
            print(-1)
        elif self.num_node == 2:
            print(-1)
        else:
            print(f"{self.head.prev} {self.head.next}")

cll = CirclyLinkedList()

city_list = list(input().split())
assert len(city_list) == num_city, "city list length error"
for city in city_list:
    cll.push_back(city)

cmd_list = []
for cmd_idx in range(num_cmd):
    cur_cmd = input()
    if len(cur_cmd) != 1:
        cur_cmd, new_city_name = cur_cmd.split()
        cmd_list.append((cur_cmd, new_city_name))
    else:
        cmd_list.append((cur_cmd, None))

for cmd in cmd_list:
    cmd, new_city_name = cmd[0], cmd[1]
    if cmd == "1":
        if CHECK:
            print("move_head_front")
        cll.move_head_front()
        cll.result_print()
    elif cmd == "2":
        if CHECK:
            print("move_head_back")
        cll.move_head_back()
        cll.result_print()
    elif cmd == "3":
        if CHECK:
            print("remove")
        cll.remove()
        cll.result_print()
    elif cmd == "4":
        if CHECK:
            print(f"add: {new_city_name}")
        cll.push(new_city_name)
        cll.result_print()
    else:
        print(f"Wrong cmd: {cmd, new_city_name}")
