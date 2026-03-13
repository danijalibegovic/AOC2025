kraj = "out"
brojPuteva = 0
max = 50

def prodji(mapa, current, visited, dac, fft, depth=0):
    if depth > max:
        return
    
    if current in visited:
        return
    
    visited.add(current)

    if current == "fft":
        fft = True
    if current == "dac":
        dac = True

    global brojPuteva
    if mapa[current][0] == kraj:
        if dac and fft:
            brojPuteva += 1
        visited.remove(current)
        return
    
    for el in mapa[current]:
        prodji(mapa, el, visited, dac, fft, depth+1)

    visited.remove(current)

put = "reactor.txt"
mapa = {}
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    for linija in linije:
        key = linija[:3]
        values = str(linija[4:]).split()
        mapa[key] = values

pocetak = "svr"
trenutni = pocetak
prodji(mapa, trenutni, set(), False, False)
print(brojPuteva)