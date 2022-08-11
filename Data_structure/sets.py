# We can't keep list, set and, dictionary in the sets

my_set = {1, 2, 3}
print(my_set)

my_set = {1.0, 'Oye', (1, 2, 3)}
print(my_set)


my_set = {1, 3}
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([2, 3, 4])
print(my_set)

my_set.update([4, 5], {1, 6, 8})
print(my_set)

my_set.discard(4)
print(my_set)

my_set.remove(6)
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)