
def dodajElemente(opseg):
    raspon = opseg.split('-')
    raspon[0] = int(raspon[0])
    raspon[1] = int(raspon[1])
    return raspon

lista = []
suma = 0
put = "test.txt"
praznoFlag = True
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    for linija in linije:
        if linija == "\n":
            praznoFlag=False
            continue
        if praznoFlag:
            lista.append(dodajElemente(linija))
        else:
            for red in lista:
                if int(linija) in range(red[0], red[1]):
                    suma+=1
                    break

print(suma)