import random 
liczba = random.randrange(100)
print("Podaj liczbe z zakresu od 0 do 100: ")
while True:
    traf = int(input())
    if traf < liczba:
        print("Za mało!!")
    elif traf>liczba:
        print("Za dużo!!")
    else:
        print("Zgadłeś!")
        break