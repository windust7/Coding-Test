n = int(input())
cur_paint = []
for _ in range(n):
    cur_row = list(map(int, input().split()))
    cur_paint.append(cur_row)

def process(paint):
    visited = [[False] * n for _ in range(n)]

    def dfs(group_num, row_idx, col_idx, group_idx):
        if row_idx <= -1 or row_idx >= n or col_idx <= -1 or col_idx >= n:
            return False
        if (not visited[row_idx][col_idx]) and (paint[row_idx][col_idx] == group_num):
            visited[row_idx][col_idx] = True
            cur_paint_group[row_idx][col_idx] = group_idx
            dfs(group_num, row_idx - 1, col_idx, group_idx)
            dfs(group_num, row_idx + 1, col_idx, group_idx)
            dfs(group_num, row_idx, col_idx - 1, group_idx)
            dfs(group_num, row_idx, col_idx + 1, group_idx)
            return True
        return False

    group_name = []
    group_idx = 0
    cur_paint_group = [[None] * n for _ in range(n)]
    for row_idx in range(n):
        for col_idx in range(n):
            if dfs(paint[row_idx][col_idx], row_idx, col_idx, group_idx):
                group_name.append((paint[row_idx][col_idx], row_idx, col_idx))
                group_idx += 1

    visited = [[0b0000] * n for _ in range(n)]
    connected_groups = [[0] * len(group_name) for _ in range(len(group_name))]

    def dfs_2(group_idx, row_idx, col_idx, direction=None):
        if row_idx <= -1 or row_idx >= n or col_idx <= -1 or col_idx >= n:
            return False
        if (cur_paint_group[row_idx][col_idx] == group_idx):
            if (not visited[row_idx][col_idx]):
                visited[row_idx][col_idx] = True
                dfs_2(group_idx, row_idx - 1, col_idx, direction=0b1000)
                dfs_2(group_idx, row_idx + 1, col_idx, direction=0b0100)
                dfs_2(group_idx, row_idx, col_idx - 1, direction=0b0010)
                dfs_2(group_idx, row_idx, col_idx + 1, direction=0b0001)
                return True
        else:
            if visited[row_idx][col_idx] & direction == 0b0000:
                connected_groups[group_idx][cur_paint_group[row_idx][col_idx]] += 1
            visited[row_idx][col_idx] = visited[row_idx][col_idx] | direction
            return True
        return False

    for group_idx, group in enumerate(group_name):
        dfs_2(group_idx, group[1], group[2])
        visited = [[0b0000] * n for _ in range(n)]

    def cal_chemi():
        result = 0
        group_num = [0 for _ in range(len(group_name))]
        for i in range(n):
            for j in range(n):
                group_num[cur_paint_group[i][j]] += 1
        for group_idx, group in enumerate(group_name[:-1]):
            for test_group in range(group_idx+1, len(group_name)):
                result += (group_num[group_idx] + group_num[test_group]) * group[0] * group_name[test_group][0] * connected_groups[group_idx][test_group]
        return result

    score = cal_chemi()
    return score

def turn_1(paint):
    n = len(paint)
    middle = (n - 1) // 2
    for idx in range(middle):
        paint[idx][middle], paint[middle][idx], paint[(n-1)-idx][middle], paint[middle][(n-1)-idx] = paint[middle][(n-1)-idx], paint[idx][middle], paint[middle][idx], paint[(n-1)-idx][middle]

def turn_2(paint):
    n = len(paint)
    middle = (n - 1) // 2

    result_paint = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result_paint[i][j] = paint[i][j]
    
    for row in range(middle):
        for column in range(middle):
            result_paint[column][middle-row-1] = paint[row][column]

    for row in range((middle+1), n):
        for column in range(middle):
            result_paint[column+middle+1][n - row - 1] = paint[row][column]
    
    for row in range(middle):
        for column in range((middle+1), n):
            result_paint[column - middle - 1][n - row - 1] = paint[row][column]
    
    for row in range((middle+1), n):
        for column in range((middle+1), n):
            result_paint[column][n - row + middle] = paint[row][column]
    
    return result_paint
    
result = 0

result += process(cur_paint)

turn_1(cur_paint)
cur_paint = turn_2(cur_paint)
result += process(cur_paint)

turn_1(cur_paint)
cur_paint = turn_2(cur_paint)
result += process(cur_paint)

turn_1(cur_paint)
cur_paint = turn_2(cur_paint)
result += process(cur_paint)

print(result)