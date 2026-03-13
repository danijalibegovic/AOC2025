put = "secretEntrance.txt"
suma = 50
brojNula = 0
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    for linija in linije:
        if linija.startswith("R"):
            suma = (suma+(int(linija[1:])))%100
        else:
            suma = (suma-(int(linija[1:])))%100
        if suma == 0:
            brojNula+=1
print(brojNula)