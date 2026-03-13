def izracunaj(matrica):
    brojDobrih=0
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            if matrica[i][j] != "@":
                continue
            brojRolnicaOko=0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if (k<0 or l<0 or k>=len(matrica) or l>=len(matrica[k]) or (k==i and l==j)):
                        continue
                    if matrica[k][l] == "@" or matrica[k][l] == "x":
                        brojRolnicaOko+=1
            if brojRolnicaOko < 4 and matrica[i][j] == "@":
                brojDobrih+=1
                matrica[i][j] = "x"
    print(brojDobrih)
    return brojDobrih


put = "printingDepartment.txt"
suma = 0

with open(put, 'r', encoding="utf-8") as file:
    matrica = [list(line.strip()) for line in file]
    suma=izracunaj(matrica)
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            print(matrica[i][j], end="")
        print()