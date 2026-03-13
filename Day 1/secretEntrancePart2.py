put = "secretEntrance.txt"
suma = 50
brojNula = 0
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    for linija in linije:
        broj = int(linija[1:])
        if linija.startswith("R"):
            brojNula+=((broj+suma)//100)
            suma = (suma+broj)%100
        else:
            if suma == 0:
                brojNula+=broj//100
            elif broj>=suma:
                brojNula+=(((broj-suma))//100)+1

            suma = (suma-broj)%100
print(brojNula)