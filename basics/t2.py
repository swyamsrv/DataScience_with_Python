from turtle import *

side = 6
size = 50
for i in range(side):
    forward(size)
    for i in range(4):
        forward(size)
        left(90)
    left(360/side)
mainloop()
