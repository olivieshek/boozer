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

        Случаи выигрыша и проигрыша:
            - кончились карты;
            - нечем ответить в споре.
"""

def make_deck() -> list(dict):
    return dict()