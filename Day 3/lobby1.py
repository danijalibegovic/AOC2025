def nadjiSumu(broj):
    najin = 0
    for i in range(len(broj)):
        if(broj[i] > broj[najin]):
            najin=i
    
    if najin == len(broj)-1:
        for novi in range(len(broj)):
            if int(broj[novi]) == int(broj[najin])-1:
                najin=novi
                break

    druginaj=najin+1
    for j in range(najin+1, len(broj)):
        if(broj[j] > broj[druginaj]):
            druginaj=j
    return int(broj[najin]+broj[druginaj])

suma = 0
put = "test.txt"
with open(put, 'r', encoding="utf-8") as file:
    linije=file.readlines()
    for linija in linije:
        suma += nadjiSumu(str(int(linija)))

print(suma)