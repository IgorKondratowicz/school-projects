import random

ilosci = [0,0,0,0,0]

for i in range(1000):
    x = random.randint(0,10000)
    if x <= 8000:
        ilosci[0]+=1
    elif x > 8000 and x <=9600: 
        ilosci[1]+=1
    elif x >9600 and x <= 9915:
        ilosci[2]+=1
    elif x > 9915 and x <= 9975:
        ilosci[3]+=1
    else:
        ilosci[4]+=1

print(
    "Ilosc niebieskich: ", ilosci[0],
    "\nIlosc fioletowych: ", ilosci[1],
    "\nIlosc rozowych: ", ilosci[2],
    "\nIlosc czerwonych: ", ilosci[3],
    "\nIlosc kos/rekawiczek: ", ilosci[4],
)
