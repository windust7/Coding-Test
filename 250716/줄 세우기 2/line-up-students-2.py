n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
class Student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

_list = [Student(students[idx][0], students[idx][1], students[idx][2]) for idx in range(n)]

_list.sort(key=lambda x: (x.height, -x.weight))

for item in _list:
    print(f"{item.height} {item.weight} {item.num}")
