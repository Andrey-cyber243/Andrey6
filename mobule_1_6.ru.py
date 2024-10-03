my_dict={'Denis':2005,'Anton':2001,'Max':2008}
print(my_dict)
print(my_dict['Anton'])
my_dict['Egor']=2006
print(my_dict)
my_dict.update({'Vasya':2006,
'Mash':1997})
print(my_dict)
del my_dict['Egor']
print(my_dict)
print(my_dict.get(2006))
print(my_dict)
my_set={1,3,4,5,2,4,5,'Egor','Egor','String',True,(4,2,5)}
print(my_set)
my_set.add(10)
my_set.add(98)
my_set.discard(5)
print(my_set)
