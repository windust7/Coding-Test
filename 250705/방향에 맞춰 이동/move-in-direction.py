n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dxy = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
x, y = 0, 0
for idx in range(n):
    cur_dir = dir[idx]
    cur_dist = dist[idx]
    x += dxy[cur_dir][0] * cur_dist
    y += dxy[cur_dir][1] * cur_dist

print(f"{x} {y}")