import itertools
import numpy as np
import pandas as pd

# 1. Dati orbitali reali: (semiasse maggiore a in UA, eccentricità e, periodo siderale T in giorni)
pianeti = {
    "Mercurio": (0.387098, 0.205630, 0.2408467 * 365.25),
    "Venere":   (0.723332, 0.006772, 0.61519726 * 365.25),
    "Terra":    (1.000000, 0.016709, 1.0000174 * 365.25),
    "Marte":    (1.523679, 0.093400, 1.8808476 * 365.25),
    "Giove":    (5.204400, 0.048900, 11.862615 * 365.25),
    "Saturno":  (9.582600, 0.056500, 29.447498 * 365.25),
    "Urano":    (19.21840, 0.046300, 84.016846 * 365.25),
    "Nettuno":  (30.11040, 0.009460, 164.79132 * 365.25)
}

# Funzione per risolvere l'Equazione di Keplero: M = E - e * sin(E)
def risolvi_keplero(M, e, iterazioni=10):
    E = M.copy()
    for _ in range(iterazioni):
        E = E - (E - e * np.sin(E) - M) / (1.0 - e * np.cos(E))
    return E

# 2. Vettore tempo sul periodo sinodico Urano-Nettuno (62.607 giorni)
#T_u, T_n = pianeti["Urano"], pianeti["Nettuno"]
T_u = pianeti["Urano"][-1]
T_n = pianeti["Nettuno"][-1]
giorni = int(np.ceil(1.0 / abs(1.0 / T_u - 1.0 / T_n)))
t = np.arange(giorni, dtype=np.float64)

# 3. Calcolo coordinate (x, y) ellittiche nel piano orbitale (Sole nell'origine)
coord = {}
for nome, (a, e, T) in pianeti.items():
    M = (2.0 * np.pi / T) * t          # Anomalia media (proporzionale al tempo)
    E = risolvi_keplero(M, e)          # Anomalia eccentrica
    
    # Posizione reale sull'ellisse con il Sole nel fuoco (0,0)
    x = a * (np.cos(E) - e)
    y = a * np.sqrt(1.0 - e**2) * np.sin(E)
    coord[nome] = (x, y)

# 4. Calcolo matrice distanze medie ellittiche (in UA)
nomi = list(pianeti.keys())
matrice_dist_medie = pd.DataFrame(0.0, index=nomi, columns=nomi)

for p1, p2 in itertools.combinations(nomi, 2):
    x1, y1 = coord[p1]
    x2, y2 = coord[p2]
    d_media = np.mean(np.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    matrice_dist_medie.loc[p1, p2] = d_media
    matrice_dist_medie.loc[p2, p1] = d_media

# 5. Calcolo tabella percentuale di vicinanza media (somma riga = 100%)
inverso_dist = 1.0 / matrice_dist_medie.replace(0.0, np.nan)
vicinanza_pct = (inverso_dist.div(inverso_dist.sum(axis=1), axis=0) * 100).fillna(0.0).round(2)

print("--- Indice di Vicinanza Media (%) - ORBITE ELLITTICHE ---")
print(vicinanza_pct.to_string())

vicinanza_pct.to_csv(r'C:\Users\msant\Desktop\planets\percentuali_ellittiche.csv')
