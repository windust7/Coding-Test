total_length = int(input())
cmd_num = int(input())
cmd_list = []
for cmd_idx in range(cmd_num):
    cur_cmd = list(map(int, input().split()))
    cmd_list.append(cur_cmd)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.data}"

def connect(first_node, second_node):
    if first_node is not None:
        first_node.next = second_node
    if second_node is not None:
        second_node.prev = first_node

node_dict = {}
for node_idx in range(1, total_length + 1):
    cur_node = Node(node_idx)
    node_dict[node_idx] = cur_node
for node_idx in range(1, total_length + 1):
    if node_idx == 1:
        pass
    else:
        cur_node = node_dict[node_idx]
        past_node = node_dict[node_idx - 1]
        connect(past_node, cur_node)


def visualize():
    for node_idx in range(1, total_length + 1):
        print(f"{node_dict[node_idx].prev} <-> {node_dict[node_idx]} <-> {node_dict[node_idx].next}")
    print()


for cmd in cmd_list:
    # print(cmd)
    first_list_start_node = node_dict[cmd[0]]
    first_list_end_node = node_dict[cmd[1]]
    second_list_start_node = node_dict[cmd[2]]
    second_list_end_node = node_dict[cmd[3]]

    # 붙어있는지 확인
    if first_list_end_node.next == second_list_start_node or second_list_end_node.next == first_list_start_node:
        is_connected = True
    else:
        is_connected = False

    if is_connected:
        if second_list_end_node.next == first_list_start_node:
            first_list_start_node, second_list_start_node = second_list_start_node, first_list_start_node
            first_list_end_node, second_list_end_node = second_list_end_node, first_list_end_node
        # breakpoint()
        first_list_prev_node = first_list_start_node.prev
        second_list_next_node = second_list_end_node.next

        if first_list_prev_node is not None:
            first_list_prev_node.next = None
            first_list_start_node.prev = None

        first_list_end_node.next = None
        second_list_start_node.prev = None

        if second_list_next_node is not None:
            second_list_next_node.prev = None
            second_list_end_node.next = None

        if first_list_prev_node is not None:
            first_list_prev_node.next = second_list_start_node
            second_list_start_node.prev = first_list_prev_node

        if second_list_next_node is not None:
            second_list_next_node.prev = first_list_end_node
            first_list_end_node.next = second_list_next_node

        second_list_end_node.next = first_list_start_node
        first_list_start_node.prev = second_list_end_node
        # visualize()

    else:
        first_list_prev_node = first_list_start_node.prev
        first_list_next_node = first_list_end_node.next
        second_list_prev_node = second_list_start_node.prev
        second_list_next_node = second_list_end_node.next

        if first_list_prev_node is not None:
            first_list_prev_node.next = None
            first_list_start_node.prev = None
        if first_list_next_node is not None:
            first_list_next_node.prev = None
            first_list_end_node.next = None
        if second_list_prev_node is not None:
            second_list_prev_node.next = None
            second_list_start_node.prev = None
        if second_list_next_node is not None:
            second_list_next_node.prev = None
            second_list_end_node.next = None

        if first_list_prev_node is not None:
            first_list_prev_node.next = second_list_start_node
            second_list_start_node.prev = first_list_prev_node
        if first_list_next_node is not None:
            first_list_next_node.prev = second_list_end_node
            second_list_end_node.next = first_list_next_node
        if second_list_prev_node is not None:
            second_list_prev_node.next = first_list_start_node
            first_list_start_node.prev = second_list_prev_node
        if second_list_next_node is not None:
            second_list_next_node.prev = first_list_end_node
            first_list_end_node.next = second_list_next_node
    # visualize()
    # print()

for node_idx in range(1, total_length + 1):
    if node_dict[node_idx].prev is None:
        cur_node = node_dict[node_idx]
        while True:
            print(cur_node, end=" ")
            if cur_node.next is None:
                break
            else:
                cur_node = cur_node.next

