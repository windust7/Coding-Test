n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

_list = [Student(name[idx], korean[idx], english[idx], math[idx]) for idx in range(n)]
_list.sort(key=lambda x: (x.korean, x.english, x.math), reverse=True)

for item in _list:
    print(f"{item.name} {item.korean} {item.english} {item.math}")