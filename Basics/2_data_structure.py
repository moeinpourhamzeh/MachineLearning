# Dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = dict()

print("dict1 b is: " , dict1['b'])
print("dict1 c is: " , dict1.get('c'))

squares = {k: v ** 2 for k, v in dict1.items()}
print("square of dict1 is: ", squares)

# Lists
list1 = ['a', 'b', 'c']
list2 = list()

print("list1 first item is:" , list1[0])
print("list1 last item is:" , list1[-1])

# Tuples, immutable lists | good for dataset rows
tuple1 = ('hello', 12, None)
tuple2 = tuple([1, 2, 3, 'jump'])

print('tuple1 second item is: ', tuple1[1])
stringfield = tuple(str(x) for x in tuple1)
print("stringified the TUPLE1: ", stringfield)

# Sets, unique items
set1 = {'a', 'b', 'c'}
set2 = set()

print('check if c exists in set1: ', 'b' in set1)