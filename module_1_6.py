my_dict = {'chetyrnadcat' : 14, 'dvadcat' : 20}
print(my_dict)
print(my_dict['chetyrnadcat'])
my_dict['shestnadcat'] = 16
print(my_dict['shestnadcat'])
my_dict.update({'sto':100, 'tysyacha':1000})
print(my_dict)
del my_dict['shestnadcat']
print(my_dict)

my_set = {1, 2, 3, 1, 3, 4, 7}
print(my_set)
my_set.add(8)
my_set.add(9)
print(my_set)
print(my_set.remove(3))