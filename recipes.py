# Домашняя работа по теме «Открытие и чтение файла, запись в файл»
# Часть про рецепты

from pprint import pprint
from random import choice
from random import randint

def get_data_from_file(filename):

    """
    Принимает в качестве аргумента имя файла, в котором содержатся записи о рецептах
    Считывает информацию из файла и преобразует ее к заданному формату
    Возвращает словарь с данными
    """

    with open(filename, encoding='utf-8') as f:
        data_list = f.read().splitlines()

    while data_list.count(''):
        data_list.remove('')

    cook_book = {}
    titles = ['ingr_name', 'quantity', 'measure']
    index_1 = 0

    while (index_1 + 1) <= len(data_list):

        if not data_list[index_1].isdigit():
            cook_book |= {data_list[index_1]: []}
            index_1 += 1

        else:
            index_2 = 1

            while index_2 <= int(data_list[index_1]):
                new_ingr_set = dict(zip(titles, data_list[index_1 + index_2].split(sep=' | ')))
                new_ingr_set['quantity'] = int(new_ingr_set['quantity'])
                cook_book[data_list[index_1 - 1]].append(new_ingr_set)
                index_2 += 1

            index_1 = index_1 + index_2

    # s = input('Хотите посмотреть меню (да/нет)? ')
    #
    # if s.lower() != 'нет':
    #     print('Вы можете заказать:')
    #     for k in cook_book:
    #         print('- ', k)

    return cook_book


def get_shop_list_by_dishes(dishes, persons):

    """
    Получает список заказанных блюд и количество персон, для которых они будут приготовлены
        Если количество персон больше заказанных блюд, то список блюд соответственно дополняется
        Если количество персон меньше заказанных блюд, то список блюд соответственно сокращается
    Запрашивает словарь с рецептами
    По каждому заказанному блюду из словаря с рецептами формирует словарь ингридиентов, необходимых для приготовления
    Формирует общий словарь ингридиентов по всем заказанным блюдам
    Количества одинаковых ингридиентов разных блюд суммируются
    Возвращает словарь ингридиентов, необходимых для приготовления всех блюд
    Если в качестве количества людей передано не целое число или не положительное целое число, то возвращается сообщение
    Также выдается сообщение о том, что заказанное блюдо отсутствует в словаре рецептов, но выполнение программы
    продолжается.
    """

    if not isinstance(persons, int) or persons <= 0:
        return 'Количество человек должно быть целым числом больше нуля'

    cook_book = get_data_from_file('recipes.txt')

    if len(dishes) < persons:                         # Если людей больше, чем блюд в списке,
        for index in range(persons - len(dishes)):    # добавляю случайные блюда из списка
            dishes.append(choice(dishes))             # чтобы блюд было столько же, сколько людей

    if len(dishes) > persons:                         # Если людей меньше, чем блюд в списке,
        for index in range(len(dishes) - persons):    # исключаю случайные блюда из списка
            del dishes[randint(0, len(dishes) - 1)]   # чтобы блюд было столько же, сколько людей

    shop_list = {}

    for index, dish in enumerate(dishes):

        new_dish = dish

        if not dish in cook_book:                               # Если заказано блюдо, которого нет в меню,
            print(f'Блюда "{dish}" нет в меню')                 # Оно будет заменено на блюдо, которое есть в меню
            new_dish = choice(list(cook_book.keys()))           # Выбор будет сделан функцией choice()
            dishes[index] = new_dish
            print(f'Поэтому блюдо "{dish}" повар заменил на "{new_dish}"\n{"-" * 25}')

        for ingr in range(len(cook_book[new_dish])):
            dish_ingr = cook_book[new_dish][ingr].copy()
            dish_ingr_name = dish_ingr['ingr_name']
            del dish_ingr['ingr_name']

            if not dish_ingr_name in shop_list:
                shop_list |= {dish_ingr_name: dish_ingr}
            else:
                shop_list[dish_ingr_name]['quantity'] += dish_ingr['quantity']

    print('\nДля приготовления заказанных блюд нужно купить:\n')
    pprint(shop_list)

    return shop_list

print()
get_shop_list_by_dishes(["Паста", "Суши", "Гамбургер", "Овсянка"], 3)
