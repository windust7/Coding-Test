n = int(input())

# Please write your code here.
cur_num = 1
for row_idx in range(n):
    for col_idx in range(n):
        print(cur_num, end=" ")
        cur_num += 1
        if cur_num == 10:
            cur_num = 1
    print()