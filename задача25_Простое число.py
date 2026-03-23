print('=' * 25)

from sympy import *

def prime_number():

    for i in my_list:
        if is_prime(i) is True:
            print(i)

def is_prime(n):
    return isprime(n)

my_list = [i for i in range(1, 101)]
if __name__ == "__main__":
    prime_number()

print('=' * 40)

def prime_number():

    for i in my_list:
        if is_prime(i) is True:
            print(i)

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

my_list = [i for i in range(1, 101)]
if __name__ == "__main__":
    prime_number()
