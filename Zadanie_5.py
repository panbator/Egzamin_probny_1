import random


def roll(liczba_kostek, typ_kostki=6, modyfikator=0):
    if typ_kostki not in [3, 4, 6, 8, 10, 12, 100]:
        raise Exception("No such dice!")

    wynik = sum(random.randint(1, typ_kostki) for _ in range(liczba_kostek))
    wynik += modyfikator

    return wynik

print(roll(2,11,20))