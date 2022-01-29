import sys

# Zugriffsversuch
try:
    e = open("SchereSteinPapier_big.in.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen aller Zeilen in eine Liste
allezeilen = e.readlines()

# Schliessen der Datei
e.close()

try:
    d = open("ausgabe2.txt","w")
except:
    print("error")
    sys.exit(0)

n = int(allezeilen[0])


wert1 = []
wert2 = []


d.close()