#Сложные условия
# 6 <= Houre < 12 - доброе утро
# 12 <= houre < 17 добрый день
# 7 <= houre < 19 добрый вечер
# pass - пройти мимо
hour = 5

if hour >= 6 and hour  < 12:
    pass
elif hour >= 12 and hour < 17:
    print('Добрый день')
elif hour >= 17 and hour < 19:
    print('Добрый вечер')
else:
    print('Доброй ночи')