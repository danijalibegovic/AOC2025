dat = "test.txt"

def ponavljaSe(n):
    rijec = str(n)
    if len(rijec)%2==0:
        srednjiIndex=len(rijec)//2
        prviDio=rijec[:srednjiIndex]
        drugiDio=rijec[srednjiIndex:]
        if prviDio==drugiDio:
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