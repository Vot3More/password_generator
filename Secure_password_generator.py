import random

quantity = int(input('Сколько паролей сгенерировать?\n'))
length = int(input('Сколько символов должно быть в пароле?\n'))
number_in_password = input('Включить ли в пароль цифры?\n')
symbol_in_password = input('Включить ли в пароль знаки?\n')
up_reg_in_password = input('Включить ли в пароль буквы ВЕРХНЕГО регистра?\n')
low_reg_in_password = input('Включить ли в пароль буквы нижнего регистра?\n')
remove_badsym = input('Исключить похожие символы il1Lo0O?\n')


def generator_password():
    password = []

    negative = [43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 64, 91, 92, 93, 94, 95, 96,
                124]  # Номер символов в таблице ASCII, которые нужно вычеркнуть
    number = [48, 49, 50, 51, 52, 53, 54, 55, 56,
              57]  # Номера цифр на случай, если пользователь не захочет иметь их в пароле
    symbol = [33, 41, 42]  # Номера знаков на случай, если пользователь не захочет иметь их в пароле
    up_reg = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
              90]  # Номера букв верхнего регистра на случай, если пользователь не захочет иметь их в пароле
    low_reg = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
               117, 118, 119, 120, 121,
               122]  # Номера букв нижнего регистра на случай, если пользователь не захочет иметь их в пароле
    badsym = ['il1Lo0O']

    while len(password) < length:
        i = random.randrange(41, 126)  # Передаем для i случайным номер из таблицы ASCII
        if i in negative:  # Если i получило номер, который нужно избегать
            continue
        else:
            # Настройка пароля в соответствии с выбором пользователя
            if i in number and number_in_password == 'да':
                password.append(chr(i))
            if i in symbol and symbol_in_password == 'да':
                password.append(chr(i))
            if i in up_reg and up_reg_in_password == 'да':
                password.append(chr(i))
            if i in low_reg and low_reg_in_password == 'да':
                password.append(chr(i))
            if i in badsym and remove_badsym.lower() == 'нет':
                password.append((chr(i)))

    random.shuffle(password)  # Перемешиваем значения в списке "пароль"
    password = ''.join(password)  # Делаем список "пароль" из одного элемента
    print(password)  # Выводим пароль пользователю


for _ in range(quantity):
    generator_password()
