num_info = int(input())
info_list = []
for _ in range(num_info):
    cur_info = tuple(input().split())
    info_list.append(cur_info)
info_list.sort(reverse=True)

print(f"name {info_list[0][0]}\naddr {info_list[0][1]}\ncity {info_list[0][2]}")