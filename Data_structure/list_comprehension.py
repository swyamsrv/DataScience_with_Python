# x = [x**2 for x in range(1, 11) if x%2== 0 ]
# print(x)

# y = [x for x in range(1, 11)]
# z = []
# for i in y:
#     sq = i**2
#     z.append(sq)
# print(y)
# print(z)    

# a = [x**3 for x in range(1, 11)]
# print(a)

# x = [1, 2, 3, 4, 5]
# y = [6, 7, 8, 9, 10]

# z = [x+y for x, y in zip(x, y)]
# print(z)
# s = []
# for i, j in zip(x, y):
#     s.append(x+y)
# print(z)
    
names = ['Bruce Wayne', 'Clark Kent', "Walley west"]
initial = []
for name in names:
    parts = name.split()
    initial.append(parts[0][0] + parts[-1][0])
print(initial)
    
compre = [name.split()[0][0]+name.split()[-1][0] for name in names]
print(compre)
