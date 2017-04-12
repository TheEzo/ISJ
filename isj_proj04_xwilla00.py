#!/usr/bin/env python3

"""
Autor: Willaschek Tomáš
xlogin: xwilla00
"""


def balanced_paren(parenstr):
    """
    vrátí True, pokud je řetězec, v němž se jako závorky mohou vyskytnout znaky '()[]{}<>', správně uzávorkovaný, jinak False
    
    :param parenstr -> řetězec, ve kterém se hledají a porovnávají závorky
    """
    # závorky které jsou použity
    brackets_l = ["{", "[", "(", "<"]
    brackets_r = ["}", "]", ")", ">"]
    res_l = []
    res_r = []
    indexes_l = []
    indexes_r = []
    # hledá pravé a levé závorky v řetězci a vloží je do pole
    for letter in parenstr:
        if letter in brackets_l:
            res_l.append(letter)
        if letter in brackets_r:
            res_r.append(letter)
    if res_r.__len__() == 0 and res_l.__len__() == 0:
        return True
    # očísluje závorky podle indexu z brackets_X do pole
    for r in res_l:
        indexes_l.append(brackets_l.index(r))
    for r in res_r:
        indexes_r.append(brackets_r.index(r))
    # otočí pole
    indexes_r = indexes_r[::-1]
    count = indexes_r.__len__()
    i = 1
    # pole a obrácené pole se musí shodovat, jinak prvky v jednom poli rotují, pokud jsou nadále odlišné, závorky jsou špatně uspořádané
    while (i <= count):
        if indexes_r == indexes_l:
            return True
        char = indexes_r[0]
        indexes_r.remove(char)
        indexes_r.append(char)
        i += 1
    return False


def caesar_list(word, key=[1, 2, 3]):
    """
    vrací vstupní řetězec zakódovaný Caesarovou šifrou
    
    :param word -> řetězec složený výhradně z 26 malých písmen anglické abecedy, jinak vrací vyjímku
    :param key -> seznam čísel, udávající posun v abecedě, použije se cyklicky, pokud není zadán, použije se defaultní klíč
    """
    # testování, jestli jsou jednotlivé znaky v rozmezí malých písmen => ASCII
    characters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","č","ě","š","ř","ž","ý","á","í","é","ů","ú"]
    for c in word:
        if c not in characters:
        #if  c != 'č' or ord(c) > ord('z') or ord(c) < ord('a'):
            raise ValueError('Bad input characters')

    key_size = key.__len__()
    i = 0
    res = ""
    # rozdělení řetězce na písmena
    for char in word:
        # pokud byl použit poslední prvek klíče, jako další se použije zase první
        if i == key_size:
            i = 0
        ascii = ord(char) + key[i]
        # ošetření, pokud znak přesáhne hodnotu 'z' nebo pokud je hodnota v klíči příliš velká
        while ascii >= 122:
            ascii -= 26
        res += chr(ascii)
        i += 1
    return res


def caesar_varnumkey(word, *key):
    """
    vrací vstupní řetězec zakódovaný Caesarovou šifrou

    :param word -> řetězec složený výhradně z 26 malých písmen anglické abecedy, jinak vrací vyjímku
    :param *key -> seznam čísel, udávající posun v abecedě, použije se cyklicky
    """
    return caesar_list(word, key)