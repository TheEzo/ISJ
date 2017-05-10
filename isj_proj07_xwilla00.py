#!/usr/bin/env python3

"""
Tomáš Willaschek (xwilla00)
proj07
"""

import math

class TooManyCallsError(Exception):
    """
    Výjimka TooManyCallsError
    """
    def __init__(self, message):
        """
        Konstruktor
        :param message: Chybová zpráva
        """
        self.message = message


def limit_calls(max_calls=2, error_message_tail='called too often'):
    """
    Dekorátor limit_calls
    :param max_calls: maximální počet volání dané funkce
    :param error_message_tail: error message, která se vypíše při překročení počtu volání
    :return: funkce pyth
    """
    def _limit_calls(func):
        def wrapper(a, b):
            if wrapper.calls < max_calls:
                wrapper.calls += 1
                ret = func(a, b)
                return ret
            else:
                specific_error_message = 'function "'+func.__name__+'" - '+str(error_message_tail)
                raise TooManyCallsError(specific_error_message)
        wrapper.calls = 0
        return wrapper
    return _limit_calls


@limit_calls(1, 'that is too much')
def pyth(a, b):
    """
    Pythagorova věta
    :param a: první číslo
    :param b: druhé číslo
    :return: výpočet Pythagorovy věty
    """
    c = math.sqrt(a**2 + b ** 2)
    return c


def ordered_merge(*args, selector=None):
    """
    Postupně generuje prvky od prvního k poslednímu podle selectoru
    :param args: ruzné iterovatelné vstupy (stringy, listy, ...)
    :param selector: pořdadí vstupů, ze kterého se generuje výstup
    :return: uvolňované prvky podle pořadí 
    """
    if selector is None:
        return []
    if selector.__len__() is 0:
        return []
    def iterate(items):
        for i in items:
            try:
                yield i
            except:
                raise StopIteration
    arr = []
    for item in args:
        arr.append(iterate(item))

    for x in range(selector.__len__()):
        yield next(arr[selector[x]])


class Log():
    """
    Třída log, která zapisuje do souboru
    """
    def __init__(self, file):
        """
        Konstruktor, otevírá soubor
        :param file: název souboru
        """
        self.f = open(file, 'w')

    def __enter__(self):
        """
        Zápis do souboru
        """
        self.f.write('Begin\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Doplní poslední řádek a zavře soubor
        """
        self.f.write('End\n')
        self.f.close()

    def logging(self, param):
        """
        Zapisuje do souboru
        """
        self.f.write(param+"\n")