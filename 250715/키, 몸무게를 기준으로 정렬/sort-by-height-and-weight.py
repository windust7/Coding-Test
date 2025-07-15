n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

_list = [Person(name[idx], height[idx], weight[idx]) for idx in range(n)]
_list.sort(key=lambda x: (x.height, -x.weight))
for item in _list:
    print(f"{item.name} {item.height} {item.weight}")