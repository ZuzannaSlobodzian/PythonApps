from src.z23 import *
from src.licznik_stanu import *

def run():
    # 6
    dane = (2024, 'Python', 3.8)
    rok, jezyk, wersja = dane

    # 7
    oceny = [4, 3, 5, 2, 5, 4]
    pierwsza, *srodek, ostatnia = oceny

    # 8
    info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')

    imie, nazwisko, _, _, zawod = info
    dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])

    # 9
    rok = dane[0]
    jezyk = dane[1][0]
    wersja = dane[1][1]
    opis = dane[1][2]

    print(opis)

    # 10, 11
    a = b = [1, 2, 3]
    c = list(a)
    b[0] = 'zmieniono'
    c[0] = 'nowa wartość'

    print(a)
    print(c)

    # 12
    x = 10
    y = x
    y = y + 1
    print(x)
    print(y)

    # 13
    K = [1, 2]
    L = K
    K = K + [3, 4]
    print(K)
    M = [1, 2]
    N = M
    print(N)
    M += [3, 4]
    print(M)

    # 14
    imiona = ['Anna', 'Jan', 'Ewa']
    oceny = [5, 4, 3]

    x = zip(imiona, oceny)

    def kwadrat(x):
        return x * x

    # 15
    liczby = [1, 2, 3, 4, 5]

    out = map(kwadrat, liczby)

    print(list(out))

    # 16
    def zmien_wartosc(arg):
        if isinstance(arg, list):
            arg[0] = "kalafior"
        if isinstance(arg, int):
            arg = 65482652

    a = 23
    print(a)
    zmien_wartosc(a)
    print(a)

    b = [1, 2, 3]
    print(b)
    zmien_wartosc(b)
    print(b)

    # 17
    def zamownie_produktu(nazwa_produktu, cena, ilosc=1):
        pass
        return "łączna kwota za zamówienie: " + nazwa_produktu + " wynosi: " + str(cena * ilosc) + " za " + str(
            ilosc) + " sztuk.", cena * ilosc

    product_list = [zamownie_produktu("frytki", 12, 2), zamownie_produktu("bakłażan", 10, 20),
                    zamownie_produktu("batat", 23, 2)]

    sum = 0
    for i in product_list:
        sum += i[1]
        print(sum)

    # 18
    def stworz_raport(*args, **kwargs):
        for a in args:
            print("dane o przedmiocie o id " + str(a) + ":")
            for k in kwargs:
                if k.find(str(a)) != -1:
                    print(kwargs[k])

    stworz_raport(101, 102, nazwa101="Kubek termiczny", cena101="45.99 zł", nazwa102="Długopis", cena102="4.99 zł")

    # 19, 21
    def stworz_funkcje_potegujaca(wykladnik: 'int') -> int:

        def poteguj(podstawa):
            return pow(podstawa, wykladnik)

        return poteguj

    potega_2 = stworz_funkcje_potegujaca(2)
    print(potega_2(4))

    #20
    wywolanie = zewnetrzna()
    print(wywolanie())
    print(wywolanie())

    print(licznik())
    print(licznik())

    l1 = Licznik()
    l1()
    l2 = Licznik()
    l2()

    licznik4.w = 0

    print(licznik4())
    print(licznik4())

    #22

    slownik_lista = [{"tytul": "Lalka", "autor": "Prus", "rok_wydania": 1890},
                     {"tytul": "Babel", "autor": "Kuang", "rok_wydania": 2023},
                     {"tytul": "Harry Potter", "autor": "Rowling", "rok_wydania": 2001}]

    sortowanie = sorted(slownik_lista, key=lambda x: x['rok_wydania'])

    for s in sortowanie:
        print(s)

    filtrowanie = filter(lambda x: x["rok_wydania"] > 2000, slownik_lista)

    nowa_lista = [f for f in filtrowanie]
    print(nowa_lista)

    tytuly_map = map(lambda x: x["tytul"], slownik_lista)

    tytuly = [t for t in tytuly_map]

    print(tytuly)

    #23
    for g in generator():
        print(g)

    gen = generator()

    print(next(gen))
    print(next(gen))
    print(next(gen))


if __name__ == "__main__":
    run()