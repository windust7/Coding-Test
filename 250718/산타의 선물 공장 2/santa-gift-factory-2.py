"""
1. n개의 벨트, m개의 물건
    1-1. 물건은 오름차순으로 올라감

2. m_src번째의 벨트에 있는 모든 물건을 m_dst번째의 벨트 제일 앞으로 옮김
    2-1. m_src번째 벨트에 물건이 없다면 무시
    2-2. 옮기고 나서 m_dst의 물건 개수를 출력

3. m_src번째의 벨트의 가장 앞에 있는 물건을 m_dst번째의 벨트의 가장 앞에 있는 물건과 교체
    3-1. 둘 중에 하나라도 물건이 없으면 옮기기만 함
    3-2. 옮기고 나서 m_dst번째 벨트의 물건 개수를 출력

4. m_src번째의 벨트에 있는 물건 개수 // 2 번째까지 있는 물건을 m_dst 번째 벨트 앞으로 옮김.
    4-1. 최대 100번 -> 최대 100,000 X 100 = 10,000,000

5. 물건의 번호가 주어질 때, (앞 물건의 번호 + 뒷 물건의 번호 * 2)를 출력
    5-1. 만약에 앞 물건이 없으면 그 번호는 -1로 대체
    5-2. 만약에 뒷 물건이 없으면 그 번호는 -1로 대체

6. 벨트 번호가 주어질 때, (그 벨트의 제일 앞에 있는 물건의 번호 + 2 * 그 벨트의 제일 뒤에 있는 물건의 번호 + 3 * 그 벨트의 물건의 개수) 출력
    6-1. 물건이 없으면 -1로 대체
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
        self.num_node = 0
    
    def push_front(self, new_node):
        if self.num_node == 0:
            self.head = new_node
            self.tail = new_node
        elif self.num_node == 1:
            connect(new_node, self.tail)
            self.head = new_node
        else:
            connect(new_node, self.head)
            self.head = new_node
        self.num_node += 1
    
    def push_back(self, new_node):
        if self.num_node == 0:
            self.head = new_node
            self.tail = new_node
        elif self.num_node == 1:
            connect(self.head, new_node)
            self.tail = new_node
        else:
            connect(self.tail, new_node)
            self.tail = new_node
        self.num_node += 1
    
    def pop_front(self):
        if self.num_node == 0:
            return None
        elif self.num_node == 1:
            return_node = self.head
            self.head = None
            self.tail = None
            self.num_node = 0
            return return_node
        else:
            return_node = self.head
            self.head = return_node.next
            self.num_node -= 1
            return return_node

first_cmd = list(map(int, input().split()))
assert first_cmd[0] == 100
num_belt, num_gift = first_cmd[1], first_cmd[2]

for cmd_idx in range(num_cmd-1):
    pass