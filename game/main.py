import random
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
suits = ('Черви', 'Бубен', 'Пики', 'Крести')

# Создание колоды
def make_deck(suits):
    deck = list()
    # генирируем общую колоду
    for suit in suits:
        for i in range(6, 15):
            card = dict()
            card["Масть"] = suit
            card["Цена"] = i
            # print('Добавили', card)
            deck.append(card)
    # перемешиваем колоду
    random.shuffle(deck)
    return deck

# TODO: как по колоде узнать, кто победит в конце

def make_hand(deck):
    # генерируем две отдельные личные колоды; 
    # раздаем карты
    for card in deck:
        user_hand = deck[:18]
        computer_hand = deck[18:]
    return list(user_hand + computer_hand)

def new_table(user_hand, computer_hand):
    table = list()
    table.append(user_hand.pop())
    table.append(computer_hand.pop())
    return table

# Игра
def new_game():
    deck = make_deck(suits)
    hand = make_hand(deck)
    user_hand = hand[0]
    computer_hand = hand[1]
    table = new_table()
    # Стол
    print(f'{table[-2]} - Ваша карта;\n{table[-1]} - карта противника.')
    # Сравним карты
        # table[-1] -> Компьютер
        # table[-2] -> Игрок
    user_card_price = table[-2]['Цена']
    computer_card_price = table[-1]['Цена']
    if user_card_price > computer_card_price:
        # Игрок выиграл
        print('Победа!')
        user_hand += table # т.к. попнули сначала,
                           # то добавляем вместе с картой игрока;
        table.clear() # чистим стол, чтобы продолжить игру.

    elif user_card_price < computer_card_price:
        # Игрок проиграл
        print('Проигрыш... :(')
        computer_hand += table # т.к. попнули сначала,
                               # то добавляем вместе с картой компа;
        table.clear() # чистим стол, чтобы продолжить игру.

    else:
        # Ничья
        print('Спор.')
        # FIXME: Должен вызвать функцию, которая приведет нас в спор
    return True

new_game()

# while user_hand and computer_hand:
#     new_round()
