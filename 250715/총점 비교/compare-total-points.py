n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

_list = [Student(name[idx], score1[idx], score2[idx], score3[idx]) for idx in range(n)]
_list.sort(key=lambda x: x.score1 + x.score2 + x.score3)

for item in _list:
    print(f"{item.name} {item.score1} {item.score2} {item.score3}")