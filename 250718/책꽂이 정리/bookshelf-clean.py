num_book, num_pocket = map(int, input().split())
num_cmd = int(input())
cmd_list = []
for cmd_idx in range(num_cmd):
    cur_cmd = list(map(int, input().split()))
    cmd_list.append(cur_cmd)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    def __str__(self):
        return f"{self.data}"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0
    
    def push_back(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def push_front(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def pop_front(self):
        if self.num == 0:
            return None
        elif self.num == 1:
            return_node = self.head
            self.head = None
            self.tail = None
            return return_node
        else:
            next_head_node = self.head.next
            cur_head_node = self.head
            disconnect(cur_head_node, next_head_node)
            self.head = next_head_node
            return cur_head_node
    
    def pop_back(self):
        if self.num == 0:
            return None
        elif self.num == 1:
            return_node = self.tail
            self.head = None
            self.tail = None
            return return_node
        else:
            next_tail_node = self.tail.prev
            cur_tail_node = self.tail
            disconnect(next_tail_node, cur_tail_node)
            self.tail = next_tail_node
            return cur_tail_node
            
dll_list = [DoublyLinkedList() for _ in range(num_pocket+1)]
node_dict = {}
for node_idx in range(1, num_book+1):
    cur_node = Node(node_idx)
    node_dict[node_idx] = cur_node
    dll_list[1].push_back(cur_node)
dll_list[1].num = num_book

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

for cmd in cmd_list:
    cmd, dll_idx_i, dll_idx_j = cmd[0], cmd[1], cmd[2]
    dll_i, dll_j = dll_list[dll_idx_i], dll_list[dll_idx_j]

    if cmd == 1:
        if dll_i.num == 0:
            pass
        elif dll_idx_i == dll_idx_j:
            next_head = dll_i.head.next
            cur_head = dll_i.pop_front()
            # disconnect(cur_head, next_head)
            dll_i.push_back(cur_head)
            # dll_i.head = next_head
        else: 
            next_head = dll_i.head.next
            cur_head = dll_i.pop_front()
            # disconnect(cur_head, next_head)
            dll_j.push_back(cur_head)
            # dll_i.head = next_head
            dll_i.num -= 1
            dll_j.num += 1
    elif cmd == 2:
        if dll_i.num == 0:
            pass
        elif dll_idx_i == dll_idx_j:
            next_tail = dll_i.tail.prev
            cur_tail = dll_i.pop_back()
            # disconnect(next_tail, cur_tail)
            dll_i.push_front(cur_tail)
            # dll_i.tail = next_tail
        else:
            next_tail = dll_i.tail.prev
            cur_tail = dll_i.pop_back()
            dll_j.push_front(cur_tail)
            dll_i.num -= 1
            dll_j.num += 1
    elif cmd == 3:
        if dll_idx_i != dll_idx_j:
            connect(dll_i.tail, dll_j.head)
            dll_j.head = dll_i.head
            dll_i.head, dll_i.tail = None, None
            dll_j.num += dll_i.num
            dll_i.num = 0

    elif cmd == 4:
        if dll_idx_i != dll_idx_j:
            connect(dll_j.tail, dll_i.head)
            dll_j.tail = dll_i.tail
            dll_i.head, dll_i.tail = None, None
            dll_j.num += dll_i.num
            dll_i.num = 0
    else:
        print(f"Wrong cmd: {cmd}")

    # for dll in dll_list[1:]:
    #     if dll.head is None:
    #         print(0)
    #     else:
    #         print(dll.num, end=" ")
    #         cur_node = dll.head
    #         while True:
    #             print(cur_node, end=" ")
    #             if cur_node == dll.tail:
    #                 print()
    #                 break
    #             else:
    #                 cur_node = cur_node.next
    # print()

for dll in dll_list[1:]:
    if dll.head is None:
        print(0)
    else:
        print(dll.num, end=" ")
        cur_node = dll.head
        while True:
            print(cur_node, end=" ")
            if cur_node == dll.tail:
                print()
                break
            else:
                cur_node = cur_node.next