def noloop(num):
    if num == 101:
        return
    print(num)
    return noloop(num+1)

noloop(1)