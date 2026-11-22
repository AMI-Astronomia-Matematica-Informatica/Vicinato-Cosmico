import itertools
import numpy as np
import pandas as pd

# 1. Dati orbitali (raggio in UA, periodo in giorni)
pianeti = {
    "Mercurio": (0.387098, 0.2408467 * 365.25),
    "Venere":   (0.723332, 0.61519726 * 365.25),
    "Terra":    (1.000000, 1.0000174 * 365.25),
    "Marte":    (1.523679, 1.8808476 * 365.25),
    "Giove":    (5.204400, 11.862615 * 365.25),
    "Saturno":  (9.582600, 29.447498 * 365.25),
    "Urano":    (19.21840, 84.016846 * 365.25),
    "Nettuno":  (30.11040, 164.79132 * 365.25)
}

# 2. Calcolo delle distanze giorno per giorno sul ciclo Urano-Nettuno
T_u, T_n = pianeti["Urano"][1], pianeti["Nettuno"][1]
giorni = int(np.ceil(1.0 / abs(1.0 / T_u - 1.0 / T_n)))
t = np.arange(giorni, dtype=np.float64)

coord = {nome: (r * np.cos(2 * np.pi / T * t), r * np.sin(2 * np.pi / T * t)) 
         for nome, (r, T) in pianeti.items()}

# 3. Costruisce la matrice delle distanze medie (in UA)
nomi = list(pianeti.keys())
matrice_dist_medie = pd.DataFrame(0.0, index=nomi, columns=nomi)

for p1, p2 in itertools.combinations(nomi, 2):
    x1, y1 = coord[p1]
    x2, y2 = coord[p2]
    d_media = np.mean(np.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    matrice_dist_medie.loc[p1, p2] = d_media
    matrice_dist_medie.loc[p2, p1] = d_media

# 4. Calcola l'indice di vicinanza media in % (inverso della distanza, somma riga = 100%)
# Sostituiamo temporaneamente lo 0 sulla diagonale con NaN per evitare divisioni per zero
inverso_dist = 1.0 / matrice_dist_medie.replace(0.0, np.nan)
vicinanza_pct = (inverso_dist.div(inverso_dist.sum(axis=1), axis=0) * 100).fillna(0.0).round(2)

print("--- Indice di Vicinanza Media (%) [Più vicino = % più alta, somma riga = 100%] ---")
print(vicinanza_pct.to_string())

vicinanza_pct.to_csv(r'C:\Users\msant\Desktop\planets\percentuali_circolari.csv')


