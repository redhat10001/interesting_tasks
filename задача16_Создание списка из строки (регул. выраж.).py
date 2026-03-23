print('*' * 25)

import re

s = 'Последняя осень ни сторчи ни слова'

RE_WORD = re.compile(r'\w+')
rez = RE_WORD.findall(s) # возможно использование s.lower() и s.upper()

print(rez)
