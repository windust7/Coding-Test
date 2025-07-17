node_num = int(input())
cmd_num = int(input())
cmd_list = []
for cmd_idx in range(cmd_num):
    cur_cmd = list(map(int, input().split()))
    if len(cur_cmd) == 2:
        cmd_list.append((cur_cmd[0], cur_cmd[1]))
    else:
        cmd_list.append((cur_cmd[0], cur_cmd[1], cur_cmd[2]))

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.data}"

node_dict = {}

for node_idx in range(1, node_num+1):
    new_node = Node(node_idx)
    node_dict[node_idx] = new_node

for cmd in cmd_list:
    if len(cmd) == 2:
        cmd, node_idx = cmd[0], cmd[1]
    else:
        cmd, node_idx_i, node_idx_j = cmd[0], cmd[1], cmd[2]
    
    if cmd == 1:
        node_i = node_dict[node_idx]
        if node_i.prev is not None and node_i.next is not None:
            prev_node = node_i.prev
            next_node = node_i.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node_i.prev = None
            node_i.next = None
        elif node_i.prev is not None and node_i.next is None:
            prev_node = node_i.prev
            prev_node.next = None
            node_i.prev = None
        elif node_i.prev is None and node_i.next is not None:
            next_node = node_i.next
            next_node.prev = None
            node_i.next = None
    elif cmd == 2:
        node_i, node_j = node_dict[node_idx_i], node_dict[node_idx_j]
        if node_i.prev is None:
            node_j.next = node_i
            node_i.prev = node_j
        else:
            original_prev_node = node_i.prev
            original_prev_node.next = node_j
            node_j.prev = original_prev_node
            node_i.prev = node_j
            node_j.next = node_i
    elif cmd == 3:
        node_i, node_j = node_dict[node_idx_i], node_dict[node_idx_j]
        if node_j.next is None:
            node_j.prev = node_i
            node_i.next = node_j
        else:
            original_next_node = node_i.next
            original_next_node.prev = node_j
            node_j.next = original_next_node
            node_j.prev = node_i
            node_i.next = node_j
    elif cmd == 4:
        node_i = node_dict[node_idx]
        if node_i.prev is None:
            print(0, end=" ")
        else:
            print(node_i.prev, end=" ")

        if node_i.next is None:
            print(0)
        else:
            print(node_i.next)
    else:
        print(f"Wrong command: {cmd}")

for node_idx in range(1, node_num+1):
    cur_node = node_dict[node_idx]
    if cur_node.next is None:
        print(0, end=" ")
    else:
        print(cur_node.next, end=" ")