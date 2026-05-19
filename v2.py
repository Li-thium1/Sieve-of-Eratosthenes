import time

n = 1000000

start = time.perf_counter()

# 1. Erstelle eine Liste, bei der der Index die Zahl darstellt.
# Am Anfang sind alle Zahlen potenziell Primzahlen (True).
ist_prim = [True] * (n + 1)
ist_prim[0] = ist_prim[1] = False # 0 und 1 sind keine Primzahlen

p = 2

# 2. Sieben bis zur Quadratwurzel von n
while p <= n ** 0.5:
    if ist_prim[p]:
        # Streiche alle Vielfachen von p (wir fangen bei p*p an)
        # range(Start, Ende, Schrittweite) geht direkt in p-Schritten durch!
        for i in range(p * p, n + 1, p):
            ist_prim[i] = False
            
    # Setze p auf die nächste Zahl
    p += 1

# 3. Am Ende sammeln wir alle Zahlen, die noch "True" sind
primzahlen = []
for i in range(2, n + 1):
    if ist_prim[i]:
        primzahlen.append(i)

end = time.perf_counter()

# Ergebnisse anzeigen
print(f"Gefundene Primzahlen: {len(primzahlen)}")
print(f"Dauer: {end - start:.4f} Sekunden")
