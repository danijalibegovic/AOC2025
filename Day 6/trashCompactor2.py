def transformiraj(lista):
    maxDuzina = 0
    for el in lista:
        if len(el) > maxDuzina:
            maxDuzina = len(el)
    
    lista_padded = []
    for el in lista:
        lista_padded.append(el.rjust(maxDuzina))
            
    rezultat = []
    
    for j in range(maxDuzina - 1, -1, -1):
        temp_num_str = ""
        for i in range(len(lista_padded)):
            char = lista_padded[i][j]
            if char != " ":
                temp_num_str += char
        
        if temp_num_str != "":
            rezultat.append(int(temp_num_str))
    print(rezultat)
            
    return rezultat

suma = 0
put = "test.txt"
sviBrojevi=[]
operacije=[]
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    brojLinije = []
    
    for i in range(3):
        brojLinije = linije[i].split()
        for broj in brojLinije:
            broj = int(broj.strip())
        sviBrojevi.append(brojLinije)
    
    operacije = linije[3].split()

for i in range(len(operacije)):
    pomocnaLista=[]
    for j in range(len(sviBrojevi)):
        pomocnaLista.append(sviBrojevi[j][i])

    zaRacun=transformiraj(pomocnaLista)

    if operacije[i] == "+":
        pomRez = sum(zaRacun)
    else:
        pomRez=1
        for broj in zaRacun:
            pomRez*=broj
    
    suma+=pomRez

print(suma)