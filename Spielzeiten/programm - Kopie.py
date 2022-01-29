import sys
# Zugriffsversuch
try:
    e = open("Spielzeiten_big.in.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen aller Zeilen in eine Liste
allezeilen = e.readlines()

# Schliessen der Datei
e.close()

try:
    d = open("ausgabe.txt","w")
except:
    print("error")
    sys.exit(0)

n = int(allezeilen[0])

lst = []
for i in range(1, n+1):
    allezeilen[i] = allezeilen[i].rstrip("\n")

    tmp = allezeilen[i].split(" ")
    tmp[0]=int(tmp[0])
    tmp[1]=int(tmp[1])
    lst.append(tmp)





lst.sort(key=lambda x: x[1])




ergebnis1 = 0
for a in range(0, n-1):

    if (lst[a][1] > lst[a+1][0]) and (lst[a][1]< lst[a+1][1]):

            if lst[a+1][1] - lst[a][0]> ergebnis1:
             ergebnis1 = lst[a+1][1] - lst[a][0]
    



print(ergebnis1)



ergebnis3 = lst[1][0]-lst[0][1]
for j in range (1, n-1):
    if (lst[j+1][0]-lst[j][1])>ergebnis3:
        ergebnis3 = lst[j+1][0]-lst[j][1]

print(ergebnis3)

d.write(str(ergebnis1)+" "+str(ergebnis3)+"\n")

d.close()








