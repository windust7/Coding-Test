command_num = int(input())
command_list = []
command_dict = {"push_back": 0, "pop_back": 1, "size": 2, "get": 3}
for _ in range(command_num):
    command = input()
    command_list.append(command)

result_list = []

def push_back(num):
    result_list.append(num)

def pop_back():
    result_list.pop()

def size():
    print(len(result_list))

def get(num):
    print(result_list[num-1])

for command in command_list:
    if command[-1].isalpha():
        if command_dict[command] == 1:
            pop_back()
        elif command_dict[command] == 2:
            size()
    else:
        command, num = command.split()
        num = int(num)
        if command_dict[command] == 0:
            push_back(num)
        elif command_dict[command] == 3:
            get(num)
