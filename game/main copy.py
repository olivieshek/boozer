import random
import time
"""
    1. Создать колоду:
        - карта (36шт.):
            -- масть (4шт. -> черви, бубны, пики, крести),
            -- цена (9шт. -> 6, 7, 8, 9, 10, 11 [Валет], 12 [Дама], 13 [Король], 14 [Туз]);
 
    2. Перемешать колоду

    3. Разделить на карты игрока и карты компьютера

    4. Раунд:
        1) Выбрасываем карту игрока
        2) Выбрасываем карту компа
        3) Сравнить карты:
            - Победа (И > К):
                -- Игрок забирает все карты на столе
            - Проигрыш (И < К):
                -- Компьютер забирает все карты на столе
            - Ничья (И = К):
                -- Выбрасываем снова

    ! Случаи выигрыша и проигрыша:
        - кончились карты;
        - нечем ответить в споре.
"""
# TODO: как по колоде узнать, кто победит в конце
# Разыгрываем раунд
def new_round(user_hand, computer_hand, table):
    user_card = {'Масть': 'Крести', 'Цена': 10} # Задаем переменную user_card,
                                # которая хранит в себе последнюю
                                # карту из user_hand,
                                # сразу удаляя ее;
    computer_card = {'Масть': 'Черви', 'Цена': 10} # То же, что и с user_card;
    # Принтим для игрока
    print('+ Ход игрока +')
    print(user_card['Цена'], user_card['Масть']) # "Красивый" принт
    table.append(user_card)
    print('\n+ Ход компьютера +')
    print(computer_card['Цена'], computer_card['Масть']) # "Красивый" принт
    table.append(computer_card)
    # input() # Пауза
    # -----
    # Сравниваем карты на столе
    # time.sleep(1)
    print('\n')
    if user_card['Цена'] > computer_card['Цена']:
        print('Вы победили!')
        for card in table:
            user_hand.insert(0, card)
            print(card['Цена'], card['Масть'], end='; ') # "Красивый" принт
    elif computer_card['Цена'] > user_card['Цена']:
        print('Вы проиграли :(')
        for card in table:
            computer_hand.insert(0, card)
            print(card['Цена'], card['Масть'], end='; ') # "Красивый" принт
    else:
        print(table, '- стол')
        print('Спор.')
            
        new_table = list()
        user_card = user_hand.pop()
        computer_card = computer_hand.pop()
        # Принтим для игрока
        print('+ Ход игрока +')
        print(user_card['Цена'], user_card['Масть']) # "Красивый" принт
        new_table.append(user_card)
        print('\n+ Ход компьютера +')
        print(computer_card['Цена'], computer_card['Масть']) # "Красивый" принт
        new_table.append(computer_card)
        table.append(new_table)
        print(table, '- стол')
        input()
            
    input('\n\nНажмите ENTER, чтобы сделать ход.')
    table.clear()

# Создаем две колоды игроков
def deal(deck, user_hand, computer_hand):
    for card in deck[:len(deck) // 2]:
        user_hand.append(card)
    for card in deck[len(deck) // 2:]:
        computer_hand.append(card)

# Создание общей колоды
def populate_deck(deck, suits):
    for suit in suits:
        for i in range(6, 15):
            card = dict()
            card["Масть"] = suit
            card["Цена"] = i
            # print('Добавили', card)
            deck.append(card)
    # перемешиваем колоду
    random.shuffle(deck)

def main():
    deck = list()
    table = list()
    user_hand = list()
    computer_hand = list()
    suits = ('Черви', 'Бубен', 'Пики', 'Крести')
    populate_deck(deck, suits)
    # print(deck)
    deal(deck, user_hand, computer_hand)
    # print(*user_hand, sep='\n')
    # print('--------------------------------')
    # print(*computer_hand, sep='\n')
    while user_hand and computer_hand:
        new_round(user_hand, computer_hand, table)
    print('>>> Результат игры <<<')
    if user_hand:
        print('Победил игрок')
    else:
        print('Победил компьютер')

main()
