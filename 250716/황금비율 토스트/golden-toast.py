bread_num, command_num = map(int, input().split())
bread_list = list(input())
command_list = []
for bread_idx in range(command_num):
    cur_command = input()
    if cur_command[0] == "P":
        command_list.append((cur_command[0], cur_command.split()[-1]))
    else:
        command_list.append((cur_command, -1))

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return f"data: {self.data}\n"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def __str__(self):
        if self.head is None:
            return "Empty DLL"
        else:
            return_str = ""
            cur_node = self.head
            while True:
                return_str += str(cur_node)
                if cur_node == self.tail:
                    break
                else:
                    cur_node = cur_node.next
            return return_str

dll = DoublyLinkedList()
for bread in bread_list:
    dll.push_back(bread)

NULL_NODE = Node(-1)
iterator = NULL_NODE

def L(iterator):
    if iterator == NULL_NODE:
        return dll.tail
    elif iterator == dll.head:
        return iterator
    else:
        return iterator.prev

def R(iterator):
    if iterator == NULL_NODE:
        return NULL_NODE
    else:
        return iterator.next

def D(iterator):
    if iterator == NULL_NODE:
        return NULL_NODE
    elif iterator == dll.tail:
        iterator.prev.next = None
        dll.tail = iterator.prev
        iterator.prev = None
        return NULL_NODE
    elif iterator == dll.head:
        iterator.next.prev = None
        dll.head = iterator.next
        iterator.next = None
        return dll.head
    else:
        return_node = iterator.next
        iterator.prev.next = iterator.next
        iterator.next.prev = iterator.prev
        iterator.next, iterator.prev = None, None
        return return_node

def P(iterator, _str):
    if iterator == NULL_NODE:
        dll.push_back(_str)
        return NULL_NODE
    elif iterator == dll.head:
        dll.push_front(_str)
        return dll.head.next
    else:
        new_node = Node(_str)
        iterator.prev.next = new_node
        new_node.next = iterator
        new_node.prev = iterator.prev
        iterator.prev = new_node
        return new_node.next

for cmd, _str in command_list:
    if cmd == "L":
        iterator = L(iterator)
    elif cmd == "R":
        iterator = R(iterator)
    elif cmd == "D":
        iterator = D(iterator)
    elif cmd == "P":
        iterator = P(iterator, _str)
    else:
        print(f"Wrong command: {cmd}, {_str}")

print_node = dll.head
while True:
    print(print_node.data, end="")
    if print_node == dll.tail:
        break
    else:
        print_node = print_node.next