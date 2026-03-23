print('*' * 25)

'''
chain умеет сцеплять генераторы.
Для реализации протокола достаточно опередить iter
В блоке else генератор "перезаряжается." 
(Это не обязательно для данного задания)
'''

from itertools import chain


class SequenceIterator:
    def __init__(self, lst: list):
        self.lst = lst
        self.iter = self._chain_gen(lst)

    @staticmethod
    def _chain_gen(lst):
        return chain(
            (el for ind, el in enumerate(lst) if not ind % 2),
            (el for ind, el in enumerate(lst) if ind % 2),
        )

    def __iter__(self):
        while self.iter:
            yield from self.iter
            self.iter = False
        else:
            self.iter = self._chain_gen(self.lst)


container = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)
