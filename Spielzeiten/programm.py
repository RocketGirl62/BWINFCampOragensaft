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
    d = open("Spielzeiten_small.out","w")
except:
    print("error")
    sys.exit(0)

n = int(allezeilen[0])
tlist = []
for i in range(1, n+1):
    allezeilen[i] = allezeilen[i].rstrip("\n")
    print(allezeilen[i])

    list = allezeilen[i].split(" ")


    print(list)




wert1 = []
wert2 = []


d.close()