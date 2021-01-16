import random
uzytkownik = 0
komp = 0
while True:
    n = str(input("wybierz orła lub reszkę, r - reszka, o - orzeł: "))
    liczba = random.choice(["r", "o"])

    if (n == "r" and liczba == "r") or (n == "o" and liczba == "o"):
        print("Trafiłeś, dodano jeden punkt!\n")
        uzytkownik +=1 
    elif n == "0": break
    else:
        print("Nie tym razem :(\n")
        komp +=1
print(
    f"Wynik uzytkownika: {uzytkownik}"
    f"\nWynik komputera: {komp}"
)    