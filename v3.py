import time

n = 1000000

start = time.perf_counter()

# 1. Sieb vorbereiten
ist_prim = [True] * (n + 1)
ist_prim[0] = ist_prim[1] = False

p = 2
while p <= n ** 0.5:
    if ist_prim[p]:
        for i in range(p * p, n + 1, p):
            ist_prim[i] = False
    p += 1

# 2. HIER werden alle einzelnen Primzahlen in einer echten Liste gesammelt
primzahlen = []
for i in range(2, n + 1):
    if ist_prim[i]:
        primzahlen.append(i) # Jede Zahl wird einzeln hinzugefügt

end = time.perf_counter()

# 3. AUSGABE: Druckt die komplette Liste aller einzelnen Primzahlen
print("Hier sind alle Primzahlen:")
print(primzahlen) 

print("\n--- STATISTIK ---")
print(f"Gefundene Primzahlen (Anzahl): {len(primzahlen)}")
print(f"Dauer: {end - start:.4f} Sekunden")
