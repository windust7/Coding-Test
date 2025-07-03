n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
finish = False
print(a[r][c], end=" ")
last = a[r][c]
while not finish:
    cur_num = a[r][c]
    ok = False
    for idx in range(4):
        if (r+dx[idx]) < 1 or (r+dx[idx]) > n or (c+dy[idx]) < 1 or (c+dy[idx]) > n:
            continue
        if cur_num < a[r+dx[idx]][c+dy[idx]]:
            r = r + dx[idx]
            c = c + dy[idx]
            print(a[r][c], end=" ")
            ok = True
            break
        if idx == 3 and not ok:
            finish = True
