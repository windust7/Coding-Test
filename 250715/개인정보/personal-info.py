N = 5
name = []
height = []
weight = []

for _ in range(N):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

_list = [Person(name[idx], height[idx], weight[idx]) for idx in range(N)]
_list.sort(key=lambda x: (x.name, -x.height))
print('name')
for item in _list:
    print(f"{item.name} {item.height} {item.weight}")
print()
_list.sort(key=lambda x: (-x.height))
print('height')
for item in _list:
    print(f"{item.name} {item.height} {item.weight}")