dat = "giftShop.txt"

def ponavljaSe(n):
    s = str(n)
    duzina = len(str(n))
    for i in range (1, (duzina//2) + 1):
        if duzina % i == 0:
            block = s[:i]
            broj_ponavljanja = duzina // i
            if block * broj_ponavljanja == s:
                return True
    
    return False

def skontajOpseg(raspon):
    lokalnaSuma = 0
    opseg = raspon.split("-")
    pocetak = int(opseg[0])
    kraj = int(opseg[1])
    for i in range(pocetak, kraj+1):
        if ponavljaSe(i):
            lokalnaSuma+=int(i)
    return lokalnaSuma

suma = 0

with open(dat, 'r', encoding="utf-8") as file:
    dijelovi = file.read()
    lista = dijelovi.split(",")
    for brojevi in lista:
        suma+=skontajOpseg(brojevi)

print(suma)