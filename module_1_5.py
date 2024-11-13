# immutable_var = 1,2,"здоровье", True
# print(immutable_var)
# immutable_var[0] = 12
# print(immutable_var)
#Значения кортежа не изменяются хоть и имеют индексацию, потому что кортеж воспринимается
 # компьютером не как раздробленный обьект а как одно целое в отличие от списка (как я  понял)
mutable_list = [1, 2, 3, "product"]
print(mutable_list)
mutable_list[0] = 200
print(mutable_list)