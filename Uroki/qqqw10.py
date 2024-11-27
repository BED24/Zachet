# цикал While

import turtle as t
from itertools import count

sides = 18
dist = 50
angle = 360 / sides

count = 0  # счетчик числа ветков цикла

while count < sides:
    t.forward(dist)
    t.right(angle)
    count += 1 # count = count + 1
else:
    print('цикл завершён')

t.mainloop()
