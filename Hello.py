pieniadzeNaStart = 50

VAT = 23

obliczonyVAT = 1 + VAT/100

cenaNetto1 = 40
cenaNetto2 = 50

cenaBrutto1 = cenaNetto1 * obliczonyVAT
cenaBrutto2 = cenaNetto2 * obliczonyVAT

pozostalePieniadze1 = pieniadzeNaStart - cenaBrutto1
pozostalePieniadze2 = pieniadzeNaStart - cenaBrutto2


print("Cena brutto produktu nr 1 wynosi ", cenaBrutto1, "zł")
print("Cena brutto produktu nr 2 wynosi ", cenaBrutto2, "zł")


print("Pieniadze pozostale po zakupie pierwszego przedmiotu: ", pozostalePieniadze1, "zł")
print("Pieniadze pozostale po zakupie drugiego przedmiotu: ", pozostalePieniadze2, "zł")
