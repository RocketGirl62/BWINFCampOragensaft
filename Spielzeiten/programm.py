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
tlist = []
lst = []
for i in range(1, n+1):
    lst = []
    allezeilen[i] = allezeilen[i].rstrip("\n")
    print(allezeilen[i])

    lst = allezeilen[i].split(" ")
    tlist = tlist + lst

    print(lst)
    print(tlist)

tlist.sort(key=lambda x: x[1])
print(tlist)



wert1 = []
wert2 = []


d.close()
