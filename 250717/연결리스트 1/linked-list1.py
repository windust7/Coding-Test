init_str = input()
cmd_num = int(input())
cmd_list = []
for cmd_idx in range(cmd_num):
    cur_cmd = input()
    if " " not in cur_cmd:
        cmd_list.append((cur_cmd, None))
    else:
        cur_cmd, cur_value = cur_cmd.split()
        cmd_list.append((cur_cmd, cur_value))

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return f"{self.data}"

target_node = Node(init_str)

for cmd, value in cmd_list:
    if cmd == "1":
        new_node = Node(value)
        if target_node.prev is None:
            target_node.prev = new_node
            new_node.next = target_node
        else:
            original_prev_node = target_node.prev
            original_prev_node.next = new_node
            new_node.prev = original_prev_node
            target_node.prev = new_node
            new_node.next = target_node
    elif cmd == "2":
        new_node = Node(value)
        if target_node.next is None:
            target_node.next = new_node
            new_node.prev = target_node
        else:
            original_next_node = target_node.next
            original_next_node.prev = new_node
            new_node.next = original_next_node
            target_node.next = new_node
            new_node.prev = target_node
    elif cmd == "3":
        if target_node.prev is not None:
            target_node = target_node.prev
    elif cmd == "4":
        if target_node.next is not None:
            target_node = target_node.next

    if target_node.prev is None:
        print("(Null)", end=" ")
    else:
        print(target_node.prev, end=" ")

    print(target_node, end=" ")

    if target_node.next is None:
        print("(Null)")
    else:
        print(target_node.next)