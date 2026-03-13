def nadjiSumu(broj, k):
    n = len(broj)
    niz = []
    kriticniIndeks = n
    sljedeciIndeks = 0
    najBroj=0
    brojac=0
    while(brojac<12):
        indeksNajveceg = sljedeciIndeks
        for i in range(sljedeciIndeks, kriticniIndeks):
            if(int(broj[i]) > najBroj):
                najBroj=int(broj[i])
                indeksNajveceg=i
        if n-indeksNajveceg>=k:
            niz.append(najBroj)
            k-=1
            sljedeciIndeks=indeksNajveceg+1
            najBroj = 0
            kriticniIndeks=n
        else:
            kriticniIndeks = indeksNajveceg
            brojac-=1
            najBroj=0
        brojac+=1

    string = ''
    for br in niz:
        string+=str(br)
    return int(string)
    
k=12
suma = 0
put = "lobby.txt"
with open(put, 'r', encoding="utf-8") as file:
    linije=file.readlines()
    for linija in linije:
        suma += nadjiSumu(str(int(linija)), k)

print(suma)