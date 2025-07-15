n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

_list = [Student(students[idx][0], students[idx][1], idx + 1) for idx in range(n)]

_list.sort(key=lambda x: (x.height, x.weight, -x.number), reverse=True)
for item in _list:
    print(f"{item.height} {item.weight} {item.number}")