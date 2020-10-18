import random
print("Hello World!")
vstup = int(input("Zadej číslo: "))
if vstup > 100:
    print("Hej, to číslo je fakt velké :-D")
elif vstup > 10:
    print("střední číslo")
else:
    print(f'tohle že je číslo?')

# druhá hra:
print("Druhá hra!")
vstup = input("Zadej jakékoliv slovo:")
delka_slova = len(vstup)
print(f'Délka tvého slova je {delka_slova} znaků.')

# třetí hra:
print(f'Myslím si nějaké číslo mezi 1 a 6')
vstup = int(input("Hádej, jaké číslo si myslím v rozmezí od 1 do 6:"))
nahodne_cislo = random.randint(1, 6)
while vstup != nahodne_cislo:
    vstup = int(input("Zkus to znovu, vyber jiné číslo v rozmezí od 1 do 6:"))
print(f'Super, trefa!')
