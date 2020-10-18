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
