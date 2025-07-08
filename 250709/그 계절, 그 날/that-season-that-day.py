Y, M, D = map(int, input().split())

# Please write your code here.
def is_yoon(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def func(year, month, day):
    if is_yoon(year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            possible = (day <= 31)
        elif month in [4, 6, 9, 11]:
            possible = (day <= 30)
        elif month == 2:
            possible = (day <= 29)
        else:
            possible = False
    else:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            possible = (day <= 31)
        elif month in [4, 6, 9, 11]:
            possible = (day <= 30)
        elif month == 2:
            possible = (day <= 28)
        else:
            possible = False
    if possible:
        if 3 <= month <= 5:
            print("Spring")
        elif 6 <= month <= 8:
            print("Summer")
        elif 9 <= month <= 11:
            print("Fall")
        else:
            print("Winter")
    else:
        print(-1)

func(Y, M, D)