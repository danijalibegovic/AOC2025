povrsina = 0
put = "movietheater.txt"
with open(put, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    brojevi = []
    for linija in linije:
        pom = linija.split(",")
        brojevi.append((int(pom[0]), int(pom[1])))

for i in range(len(brojevi)):
    for j in range(len(brojevi)):
        x_dist = abs(brojevi[i][0] - brojevi[j][0]) + 1
        y_dist = abs(brojevi[i][1] - brojevi[j][1]) + 1
        s = x_dist*y_dist
        if s>povrsina:
            povrsina=s

print(povrsina)