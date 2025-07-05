length, total_turn = map(int, input().split())
up_list = list(map(int, input().split()))
down_list = list(map(int, input().split()))

for turn_idx in range(total_turn):
    up_to_down = up_list[-1]
    down_to_up = down_list[-1]
    for idx in range(length-1, 0, -1):
        up_list[idx] = up_list[idx-1]
        down_list[idx] = down_list[idx-1]
    up_list[0] = down_to_up
    down_list[0] = up_to_down
for up_item in up_list:
    print(up_item, end=" ")
print()
for down_item in down_list:
    print(down_item, end=" ")