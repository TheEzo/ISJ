#!/usr/bin/env python3

"""
Autor: Tomáš Willaschek
XLogin: xwilla00
"""

class Polynomial:
    """
    Polynomial
    Pracuje s polynomy, nad kterými provádí určité operace
    """
    def __init__(self, *args, **kwargs):
        """
        Konstruktor
        :param args: parametr zadaný pomocí hodnot nebo pole
        :param kwargs: parametr zadaný pomocí 'x0=5, ...'
        :return: nastaví objekt (pole) self.args na hodnotu zadanou parametrem
        """
        # kontrola vstupního řetězce, jestli je to pole hodnot, hodnoty nebo hodnoty zadané klíčem
        if str(args)[:2] == "([":
            # pole se otáčí z důvodu smazání zbytečných nul, stejně jako v dalších ifech
            self.args=list(reversed(args[0]))
        elif kwargs.__len__() is 0:
            self.args=list(reversed(args))
        else:
            # seřadí je podle indexu
            keys=tuple(sorted(kwargs.keys(), reverse=True))
            # numb = největší index (x^9 => numb = 9)
            numb=int(keys[0][1:])+1
            pom = [0] * numb
            # doplní list hodnot o nezadané hodnoty nulou, následně vrací nové pole
            for k in keys:
                pom[numb-1-int(k[1:])]=kwargs.get(k)
            self.args=list(pom)
        # odstranění nul na začátku pole, nemá smysl mít v poli ... + 0x^20 + 0x^21 + ...
        while True:
            if self.args.__len__() is not 0 and self.args[0] is 0:
                self.args.remove(0)
            else:
                break
        # uloží do objektu obrácené pole, obrácené z důvodu jednoduchosti výpočtu
        self.args=list(reversed(self.args))

    def __str__(self):
        """
        Upraví objekt na řetězec upravený pro tisk na obrazovku
        :return: tisknutelný string
        """
        if self.args.__len__() is 0:
            return "0"
        res=[]
        i = 0
        # naformátuje každý prvek (přidá x^... a znaménko) a uloží do pole
        for v in self.args:
            if v is not 0:
                if int(v) < 0:
                    sign="- "
                    v*=-1
                else:
                    sign="+ "
                if i is 0:
                    res.append(str(sign) + str(v))
                elif i is 1:
                    res.append(str(sign) + str("" if v is 1 else v) + "x")
                else:
                    res.append(str(sign) + str("" if v is 1 else v) + "x^" + str(i))
            i += 1
        if res.__len__() is 0:
            return "0"
        # pole se otočí a spojí v řetěžec, který je návratovou hodnotou
        res = list(reversed(res))
        res = " ".join(res)
        # aby řetězec nezačínal "+ ..."
        if res[:1] is "+":
            return res[2:]
        return res

    def __eq__(self, other):
        """
        Zjistí, jestli jsou objekty (hodnoty) shodné
        :param other: pole k porovnání
        :return: true/false jestli jsou shodné/neshodné
        """
        if self.args == other:
            return True
        return False

    def __add__(self, other):
        """
        Sčítá 2 objekty 
        :param other: objekt k přičtení
        :return: Objekt s hodnotami původního objektu + druhého objektu
        """
        # vytvoří pole 0 o velikosti dělšího z parametrů
        if self.args.__len__() > other.args.__len__():
            pom = [0] * self.args.__len__()
        else:
            pom = [0] * other.args.__len__()
        pol1 = self.args
        pol2 = other.args
        # kratší z polí prodlouží, aby se délky polí rovnaly
        if pol1.__len__() < len(pom):
            for i in range(len(pom) - pol1.__len__()):
                pol1.append(0)
        if pol2.__len__() < len(pom):
            for i in range(len(pom) - pol2.__len__()):
                pol2.append(0)
        # sčítání položek polí
        for x in range(len(pom)):
            pom[x]=pol1[x]+pol2[x]
        return Polynomial(pom)

    def __pow__(self, power, modulo=None):
        """
        Funkce exponent: spočítá x-tou mocninu objektu
        :param power: nezáporné číslo, exponent
        :param module: není použito
        :return: vrací objekt s hodnotami umocněné funkce self.args
        """
        # kontrola mocniny
        if power < 0:
            raise ValueError('Mocnina musí být nezáporné číslo!')
        if power is 0:
            return Polynomial(1)
        if power is 1:
            return Polynomial(self.args)
        pom2 = self.args
        # počet umocňování (**2 -> pole se vynásobí samo sebou jen jednou)
        for i in range(power-1):
            pom = []
            # násobení pole sama sebou, každý prvek uložený do pomocného pole pom2 se vynásobí původnímm polem (self.args)
            # pom2 se přepíše novou hodnout a násobí se znova, pokud je splněna podmínka prvního foru
            for j in range(self.args.__len__()):
                # vynulování proměnné, do které se ukládá průbězné roznásobení
                x = []
                # násobení k-té položky pom2 self.args[0-velikost]
                for k in range(pom2.__len__()):
                    x.append(pom2[k]*self.args[j])
                # při druhém a víc procházení je nutné pole posunout o jednu hodnotu
                x = [0]*j + x
                # nastavení velikosti větším z polí a rozšíření druhého
                if x.__len__() < pom.__len__():
                    velikost=pom.__len__()
                    x = x + [0] * (velikost - x.__len__())
                else:
                    velikost=x.__len__()
                    pom = pom + [0] * (velikost - pom.__len__())
                # pom slouží k uložení roznásobeneného pole, každou další iterací mocniny se nuluje
                for k in range(velikost):
                    pom[k]= pom[k]+x[k]
            # nastavení velikosti větším z polí a rozšíření druhého
            if pom2.__len__() < pom.__len__():
                velikost = pom.__len__()
                pom2 = pom2 + [0] * (velikost - pom2.__len__())
            else:
                velikost = pom2.__len__()
                pom = pom + [0] * (velikost - pom.__len__())
            # uložení nové hodnoty do pom2
            for j in range(velikost):
                pom2[j] = pom[j]
        return Polynomial(pom)

    def derivative(self):
        """
        Derivace: zderivuje objekt
        :return: vrací nový objekt s výsledkem derivace
        """
        li=[]
        # začíná od konce, násobí položku objektu self koeficientem, na kterém místě se nachází
        for i in range(self.args.__len__()):
            li.append(self.args[i] * i)
        # poslední položka je číslo, derivace konstanty = 0
        li.remove(li[0])
        return Polynomial(li)

    def at_value(self, val1, val2=0):
        """
        Spočítá hodnotu x
        :param val1: hodnota dosazená za x
        :param val2: nemusí být zadána, hodnota dosazená za x
        :return: vrací výsledek, pokud val2 je nenulové, vrací výpočet s drouhou hodnotou minus výpočet s první hodnotou
        """
        res1 = 0
        i = 0
        # dosadí za aktuální index x (x^0 až x^velikost_pole) a přičte výsledek do proměnné
        for v in self.args:
            if i is 0:
                res1 += v
            else:
                res1 += v * val1**i
            i += 1
        # pokud je druhá hodnota nenulová, provádí se identická první funkce
        if val2 is not 0:
            res2=0
            i = 0
            for v in self.args:
                if i is 0:
                    res2 += v
                else:
                    res2 += v * val2 ** i
                i += 1
            return res2-res1
        else:
            return res1


def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
