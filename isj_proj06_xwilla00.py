#!/usr/bin/env python3

from itertools import permutations


"""
Projekt číslo 6
Autor: Tomáš Willaschek
Login: xwilla00
Datum: 12. 4. 2017
"""

def first_nonrepeating(s):
    """
    Funkce hledá první neopakující se znak v řetězci
    :param s: vstupní řetězec, ve kterém se hledá znak
    :return: první neopakující se znak, nebo None
    """
    characters = []
    removed = []
    # pokud znak není v prvním poli, je přidám
    # pokud už se v prvním poli nachází, odstraní se a přidá se do druhého pole - tzn: znak se opakuje vícekrát
    for c in s:
        if c in characters:
            characters.remove(c)
            removed.append(c)
        elif c in removed:
            pass
        else:
            characters.append(c)
    if characters:
        return characters[0]
    return None


def combine4(numbs, result):
    """
    Funkce hledá všechny kombinace z čísel 'numbs', které se rovnají 'result'
    :param numbs: pole čísel
    :param result: výsledek na porovnání
    :return: pole výsledků, popřípadě None
    """
    operators = ["+", "-", "*", "/"]
    to_count = []
    res = []

    for n in permutations(numbs, 4):
        # první operátor
        for i in range(4):
            # druhý operátor
            for j in range(4):
                # třetí operátor
                for k in range(4):
                    # xxxx - x reprezentuje číslo, mezi čísly je operátor
                    to_count.append(str(n[0]) + operators[i] + str(n[1]) + operators[j] +
                                    str(n[2]) + operators[k] + str(n[3]))
                    # (xx)xx
                    to_count.append("(" + str(n[0]) + operators[i] + str(n[1]) + ")" +
                                    operators[j] + str(n[2]) + operators[k] + str(n[3]))
                    # xx(xx)
                    to_count.append(str(n[0]) + operators[i] + str(n[1]) + operators[j] + "("
                                    + str(n[2]) + operators[k] + str(n[3]) + ")")
                    # x(xx)x
                    to_count.append(str(n[0]) + operators[i] + "(" + str(n[1]) + operators[j]
                                    + str(n[2]) + ")" + operators[k] + str(n[3]))
                    # (xx)(xx)
                    to_count.append("(" + str(n[0]) + operators[i] + str(n[1]) + ")" +
                                    operators[j] + "(" + str(n[2]) + operators[k] + str(n[3]) + ")")
                    # ((xx)x)x
                    to_count.append("((" + str(n[0]) + operators[i] + str(n[1]) + ")" + operators[j] + str(
                        n[2]) + ")" + operators[k] + str(n[3]))
                    # x(x(xx))
                    to_count.append(str(n[0]) + operators[i] + "(" + str(n[1]) + operators[j] + "(" + str(
                        n[2]) + operators[k] + str(n[3]) + "))")
                    # x((xx)x)
                    to_count.append(str(n[0]) + operators[i]+ "((" + str(n[1]) + operators[j] + str(
                        n[2]) + ")" + operators[k] + str(n[3]) + ")")
                    # (x(xx))x
                    to_count.append("(" + str(n[0]) + operators[i] + "(" + str(n[1]) + operators[j] + str(
                        n[2]) + "))" + operators[k] + str(n[3]))
                    # (xxx)x
                    to_count.append("(" + str(n[0]) + operators[i] + str(n[1]) + operators[j] + str(
                        n[2]) + ")" + operators[k] + str(n[3]))
                    # x(xxx)
                    to_count.append(str(n[0]) + operators[i] + "(" + str(n[1]) + operators[j] + str(
                        n[2]) + operators[k] + str(n[3]) + ")")
    to_count2 = []
    # odstraní duplicity vzniklé při permutacích
    for i in to_count:
        if i not in to_count2:
            to_count2.append(i)
    # porovná hodnotu s výsledkem a přidá do pole
    for i in range(to_count2.__len__()):
        try:
            if eval(to_count2[i]) == result:
                res.append(to_count2[i])
        except ZeroDivisionError:
            pass
    if res:
        return res
    return None