print('=' * 25)

from itertools import groupby


def compress_string(string: str) -> str:
    temp = ''.join(f'{key}{len(list(group))}' for key, group in groupby(string.lower()))

    return temp if len(temp) < len(string) else string


# Тестовые случаи с корректными входными данными
assert compress_string("aaaabbbc") == "a4b3c1"
assert compress_string("abbbbbd") == "a1b5d1"

# Тестовые случаи с длинной строки
assert compress_string("a" * 1000000) == "a1000000"
assert compress_string("a" * 1000000 + 'b' * 500) == "a1000000b500"
assert compress_string("abcdefghijk" + "w" * 10000) == "a1b1c1d1e1f1g1h1i1j1k1w10000"
