
def dodajElemente(opseg):
    raspon = opseg.split('-')
    raspon[0] = int(raspon[0])
    raspon[1] = int(raspon[1])
    return (raspon[0], raspon[1])

def spojiIntervale(lista):
    lista = sorted(lista, key = lambda x: x[0])
    spojena = [lista[0]]
    for pocetak, kraj in lista[1:]:
        zadnjiPocetak, zadnjiKraj = spojena[-1]
        if pocetak <= zadnjiKraj+1:
            spojena[-1] = (zadnjiPocetak, max(zadnjiKraj, kraj))
        else:
            spojena.append((pocetak, kraj))
    return spojena

lista = []
put = "cafeteria.txt"
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    for linija in linije:
        if linija == "\n":
            break
        lista.append(dodajElemente(linija))


spojena = spojiIntervale(lista)
ukupno = sum(kraj-pocetak+1 for pocetak, kraj in spojena)
print(ukupno)