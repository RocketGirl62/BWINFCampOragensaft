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


lst.sort(key=lambda x: x[1])
print(lst)



wert1 = []
wert2 = []


d.close()
