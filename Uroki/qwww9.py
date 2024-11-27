# отрицание (инвектор)
# 1 not - нет
# 2 and - и
# 3 or - или

flag = False

if flag:
    print('Включен')
else:
    print('Выключен')

print('Нажали кнопку')
flag = not flag

if flag:
    print('Включен')
else:
    print('Выключен')
