x= chr(65)
print(x)
x = chr(555)
print(x)
x = chr(2365)
print(x)
x = chr(12365)
print(x)

for i in range(1, 127):
    print(chr(i), '=', ord(chr(i)), end=' | ')
    
print(len('amazing'))
print(len('world'))
