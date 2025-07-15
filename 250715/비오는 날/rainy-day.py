n = int(input())
date = []
day = []
weather = []

min_idx = int(1e9)
min_year = "9999-99-99"
for idx in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
    if w == "Rain":
        if min_year > d:
            min_year = d
            min_idx = idx

print(f"{date[min_idx]} {day[min_idx]} {weather[min_idx]}")

# Please write your code here.