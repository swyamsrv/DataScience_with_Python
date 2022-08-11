

my_tuple = (1, 'Hello', 3.4)
print(my_tuple)

my_tuple = ('mouse', [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple = 3, 4.6, 'apple'
print(type(my_tuple))


my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])

n_tuple = ("mouse", [8,4,6], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])


my_tuple = ('e', 'x', 'c', 'a', 'l', 'i', 'b', 'u', 'r')
print(my_tuple[1:4])

print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

print((1, 2, 3)+(4, 5, 6))

print(('Repeat',) *3)

my_tuple = ('a', 'p', 'p', 'l', 'e', )
print(my_tuple.count('p'))
print(my_tuple.index('l'))