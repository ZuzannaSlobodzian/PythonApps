import json
import math
import random

wartosc = 100
dodawanie = wartosc + 123.15
potega = pow(dodawanie, 12)
print(potega)
# potega = dodawanie**12345
tekst = str(potega)
wartosc_pi = math.pi
losowa = [1, 2, 3, 4, 5]
print(random.choice(losowa))

tekst = f"Wartosc: {tekst}"
print(len(tekst))
print(tekst[1:4])
print(dir(tekst))
print(tekst.upper())
tekst = tekst.replace(tekst[2], 'p')
print(tekst)

lista = list(tekst)
lista = lista[0:8]

lista = lista + [1, 2, 3, 4, 5]
print(lista)
lista.remove(":")
print(lista)
lista2 = [1, 2, 3, "banan", 100]

lista3 = [x ** 2 for x in lista2 if x != "banan"]
print(lista3)
lista4 = [i for i in range(4, 16, 2)]
print(lista4)

ja = {'imie': 'izabela', 'nazwisko': 'lecka', 'wiek': 25, 'rodzice':
    {'ojciec': {'imie': 'tomasz', 'wiek': 64}, 'matka': {'imie': 'iwona', 'wiek': 34}}}

print(ja['rodzice'])
print(ja['rodzice']['ojciec']['imie'])
print(ja.keys())
print(ja.get('rodzenstwo'))

bool = 'rodzenstwo' in ja
print(bool)

krotka1 = (1, 2, "3", 4, 2, 5)
print(len(krotka1))
print(krotka1[0])
print(krotka1.count(2))

X = set("kalarepa")
Y = set("lepy")
print(X.intersection(Y))

imiona = ['ada', 'ala', 'lala']

k = 0
for i in imiona:
    print(i, " ", k)
    k = k + 1

print(list(enumerate(imiona)))

l = 5
if l % 2 == 0 & l > 0:
    print("Liczba jest dodatnia i parzysta")
else:
    if l != 0:
        print("Liczba jest różna od zera")

owoce = ['jablko', 'banan', 'moreletrele']
woc = 'banan'
if woc in owoce:
    print("Owoc jest dostępny")

# sum = 0
# while sum < 100:
#     liczba = int( input())
#     sum = sum + liczba
#
# print(sum)

L = [1,2,3,4]
M = [1,2,3,L,4]
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow"
print(f"Wartość zmiennej M po zmianie L: {M}")

L = [4,5,6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")
L = [4,5,6]
Y = [list(L)] * 4
L[1] = "wow"
print(f"Y: {Y}")
Y[0][1] = "wow"
print(f"Y: {Y}")


with open('teksty.json', 'r') as file:
    content = file.read()

print(content)

text = json.loads(content)
print(text)
bigString = ""
for e in text['teksty']:
    sub = str(e.values()).split("'")
    bigString = bigString + " " + sub[1]

print(bigString)

bigString = bigString.lower();
print(bigString)

listAnna = bigString.split(" ")
listAnna.pop(0)

print(listAnna)

listAnna = [e.replace(".", "") for e in listAnna]
listAnna = [e.replace(",", "") for e in listAnna]
listAnna = [e[0:-1]+e[-1].upper() for e in listAnna]
print(listAnna)
listAnna = [e for e in listAnna if e.find("a") != -1 or e.find("A") != -1]

print(listAnna)

listAnnaS = list(dict.fromkeys(listAnna))

print(listAnnaS)

dictAnna = {}
for e in listAnnaS:
    dictAnna[e] = listAnna.count(e)

print(dictAnna)

with open("output.json", "w") as outfile:
    json.dump(dictAnna, outfile)