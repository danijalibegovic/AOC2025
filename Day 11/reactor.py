kraj = "out"
brojPuteva = 0

def prodjiRekurzivno(mapa, current):
    global brojPuteva
    if mapa[current][0] == kraj:
        brojPuteva += 1
        return
    for el in mapa[current]:
        prodjiRekurzivno(mapa, el)

put = "reactor.txt"
mapa = {}
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    for linija in linije:
        key = linija[:3]
        values = str(linija[4:]).split()
        mapa[key] = values

pocetak = "you"
trenutni = pocetak
prodjiRekurzivno(mapa, trenutni)
print(brojPuteva)