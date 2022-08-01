# Getting a slice

s = 'digipodium'
slice = s[4:7]
print(slice)

slice1 = s[:4]
slice2 = s[0:7]
print(slice1, slice2)

slice3 = s[4:]
slice4 = s[4: len(s)]
print(slice3, slice4)

name = 'Swyam Srivastava'
first = name[:5]
last = name[-10:]
even = name[::2]
odd = name [1::2]
print(first)
print(last)
print(even)
print(odd)
rever = name[::-1]
print(rever)

differ = name[::-1][:10][::-1]
print(differ)

leave3 = name[3:-3]
print(leave3)