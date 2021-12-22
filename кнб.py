import random


def rps():
    random_item = random.choice(['Камень', 'Ножницы', 'Бумага'])
    random_item = random_item.upper()
    item = input('Камень, ножницы или бумага? ').upper()

    if item == 'НОЖНИЦЫ':
        wrong = False
    elif item == 'КАМЕНЬ':
        wrong = False
    elif item == 'БУМАГА':
        wrong = False
    else:
        wrong = True

    if wrong != True:
        if random_item == 'КАМЕНЬ' and item == 'КАМЕНЬ':
            print(f'Противник выбрал {random_item.lower()}, Ничья! ')

        else:
            if random_item == 'КАМЕНЬ' and item != 'КАМЕНЬ':
                if item == 'БУМАГА':
                    print(f'Противник выбрал {random_item.lower()}, Вы выйграли! ')

                else:
                    print(f'Противник выбрал {random_item.lower()}, Вы проиграли! ')

    else:
        i = 1

    if wrong != True:
        if random_item == 'БУМАГА' and item == 'БУМАГА':
            print(f'Противник выбрал {random_item.lower()}, Ничья! ')

        else:
            if random_item == 'БУМАГА' and item != 'БУМАГА':
                if item == 'НОЖНИЦЫ':
                    print(f'Противник выбрал {random_item.lower()}, Вы выйграли! ')

                else:
                    print(f'Противник выбрал {random_item.lower()}, Вы проиграли! ')

    else:
        i = 1

    if wrong != True:
        if random_item == 'НОЖНИЦЫ' and item == 'НОЖНИЦЫ':
            print(f'Противник выбрал {random_item.lower()}, Ничья! ')

        else:
            if random_item == 'НОЖНИЦЫ' and item != 'НОЖНИЦЫ':
                if item == 'КАМЕНЬ':
                    print(f'Противник выбрал {random_item.lower()}, Вы выйграли! ')

                else:
                    print(f'Противник выбрал {random_item.lower()}, Вы проиграли! ')

    else:
        i = 1

    if wrong == True:
        print('Ошибка ввода ')


def repeat():
    check = input('Продолжить? да / нет ').upper()
    if check == 'ДА':
        state = True
    elif check == 'НЕТ':
        state = False
    else:
        state = False
        print('Ошибка ввода')
    return state


rps()

while repeat() == True:
    print(' ')
    rps()
