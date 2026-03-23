import random


def main():

    # создать колоду
    deck = create_deck()

    # получить количество карт
    num_card = int(input('Введите количество карт для раздачи: '))
    # раздать карт
    dial_card(deck, num_card)


def create_deck():
    picki = [
        'туз п',
        'двойка п',
        'тройка п',
        'четверка п',
        'пятерка п',
        'шестерка п',
        'семерка п',
        'восьмерка п',
        'девятка п',
        'десятка п',
        'валет п',
        'дама п',
        'король п',
    ]
    trefa = [
        'туз т',
        'двойка т',
        'тройка т',
        'четверка т',
        'пятерка т',
        'шестерка т',
        'семерка т',
        'восьмерка т',
        'девятка т',
        'десятка т',
        'валет т',
        'дама т',
        'король т',
    ]
    bubi = [
        'туз б',
        'двойка б',
        'тройка б',
        'четверка б',
        'пятерка б',
        'шестерка б',
        'семерка б',
        'восьмерка б',
        'девятка б',
        'десятка б',
        'валет б',
        'дама б',
        'король б',
    ]
    chervi = [
        'туз ч',
        'двойка ч',
        'тройка ч',
        'четверка ч',
        'пятерка ч',
        'шестерка ч',
        'семерка ч',
        'восьмерка ч',
        'девятка ч',
        'десятка ч',
        'валет ч',
        'дама ч',
        'король ч',
    ]
    cena = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    picki = dict(zip(picki, cena))
    trefa = dict(zip(trefa, cena))
    bubi = dict(zip(bubi, cena))
    chervi = dict(zip(chervi, cena))
    deck = {}
    deck.update(picki)
    deck.update(trefa)
    deck.update(bubi)
    deck.update(chervi)
    return deck


def dial_card(deck, number):
    count_hand = 0

    if number > len(deck):
        number = len(deck)

    for count in range(number):
        card, values = deck.popitem()
        print(card)
        count_hand += values

    print(f'величина карт на руках: {count_hand}')


main()
