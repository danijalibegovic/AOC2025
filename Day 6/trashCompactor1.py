suma = 0
put = "trashCompactor.txt"
sviBrojevi=[]
operacije=[]
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    brojLinije = []
    
    for i in range(4):
        brojLinije = linije[i].split()
        for broj in brojLinije:
            broj = int(broj.strip())
        sviBrojevi.append(brojLinije)
    
    operacije = linije[4].split()

for i in range(len(operacije)):
    podRezMul = 1
    podRezAdd = 0
    for j in range(len(sviBrojevi)):
        if operacije[i] == "+":
            podRezAdd+=int(sviBrojevi[j][i])
        else:
            podRezMul*=int(sviBrojevi[j][i])
    suma+=podRezAdd
    if podRezMul!=1:
        suma+=podRezMul

print(suma)