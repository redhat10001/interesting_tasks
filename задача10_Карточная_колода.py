print('*' * 25)

cards2 = {}
ranks = [str(n) for n in range(2, 11)] + list('ВДКТ')
suits = 'трефы буби пики черви'.split()
cards = {f'{rank} {suit}': rank for suit in suits for rank in ranks}
cards2 = {suit: (10 if value in 'ВДК' else 11 if value == 'Т' else int(
    value)) for suit, value in cards.items()}
print(cards2)
