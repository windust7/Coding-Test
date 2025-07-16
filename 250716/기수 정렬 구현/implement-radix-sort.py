n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for cur_idx in range(6):
    if cur_idx == 0:
        cur_list = [[] for _ in range(10)]
        for item in arr:
            cur_list_idx = item % 10
            cur_list[cur_list_idx].append(item)
    else:
        next_list = [[] for _ in range(10)]
        for cur_list_idx in cur_list:
            for item in cur_list_idx:
                next_list_idx = str(item % (10 ** (cur_idx+1)))
                if len(next_list_idx) < (cur_idx+1):
                    next_list_idx = 0
                else:
                    next_list_idx = int(next_list_idx[0])
                next_list[next_list_idx].append(item)
        cur_list = next_list


for cur_list_idx in cur_list:
    for item in cur_list_idx:
        print(item, end=" ")
