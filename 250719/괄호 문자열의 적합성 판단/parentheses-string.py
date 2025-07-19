str_input = input()

# Please write your code here.
_list = []
result = True
for _str in str_input:
    if _str == "(":
        _list.append("(")
    else:
        if len(_list) == 0:
            result = False
            break
        else:
            _list.pop()
    
if result and len(_list) == 0:
    print("Yes")
else:
    print("No")