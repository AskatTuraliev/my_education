first = int(input('ВВедите число 1: '))
second = int(input('ВВедите число 2: '))
third = int(input('ВВедите число 3: '))
if first == second and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)