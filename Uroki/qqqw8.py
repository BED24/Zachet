# and - и , or - или

string = ''

name = input('Как Ваше имя:')
surname = input('Как ваше фамилия:')
age = input('Ваш Возраст:')
gender = input('Укажите пол (М или Ж):')

if name == 'Вася' and surname == 'Пупкин':
    print('Уважайте свое имя!!!')
else:
            # Основное условие
    if (gender == 'М' or gender == 'м' or gender == 'v'
            or gender == 'V'):
        string = 'Уважаемый '
    elif (gender == 'Ж' or gender == 'ж'
          or gender == ';'):
        string = 'Уважаеая '
    else:
        string = 'Уважаемый товарищ '
    string = (string + name + ' ' + surname + ' ' +
              'Ваш возраст: ' + age + '.')
            # конец
print(string)
