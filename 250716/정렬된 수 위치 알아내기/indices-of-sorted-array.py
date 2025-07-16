n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
sorted_sequence = sorted(sequence)
item_count = {}
item_current_count = {}
for item in sorted_sequence:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1
        item_current_count[item] = 0

for item in sequence:
    cur_idx = sorted_sequence.index(item) + 1 + item_current_count[item]
    item_current_count[item] += 1
    print(f"{cur_idx}", end = " ")
    