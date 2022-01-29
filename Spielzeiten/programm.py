import sys
# Zugriffsversuch
try:
    e = open("Spielzeiten_small.in.txt")
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
    print(allezeilen[i])
    tmp = allezeilen[i].split(" ")
    tmp[0]=int(tmp[0])
    tmp[1]=int(tmp[1])
    lst.append(tmp)
    print(lst)




lst.sort(key=lambda x: x[0])
print(lst)
a = 0
ergebnis = 0
while a < n:#for a in range(0,n):
    anfangszeit = lst[a][0]
    for j in range(a, n): 
        if lst[j][1] <= lst[j][0]:
            a = a +1
        else:
            if ergebnis < (lst[j][0] - anfangszeit):
                ergebnis = lst[j][0] - anfangszeit
            a = a+1
            break

print(ergebnis)





d.close()
