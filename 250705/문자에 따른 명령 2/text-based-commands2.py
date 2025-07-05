row, col, direction = 0, 0, 0

commands = list(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for command in commands:
    if command == "L":
        direction = (direction - 1 + 4) % 4
    elif command == "R":
        direction = (direction + 1) % 4
    elif command == "F":
        row += dx[direction]
        col += dy[direction]

print(f"{col} {row}")