**Vicinato Cosmico**
Analisi geometrica e temporale delle distanze nel Sistema Solare

Laboratorio digitale **AMI** (*Astronomia, Matematica, Informatica*) — a cura di **Massimiliano Santini**.

---

## Panoramica
Analizzando la dinamica orbitale lungo un intero periodo sinodico Urano–Nettuno (**171 anni**, 62.607 giorni), si dimostra come **Mercurio** sia in media il pianeta più vicino non solo alla Terra, ma a ciascuno degli altri pianeti del Sistema Solare.

Aggiornamenti

28/11/2026: Articolo Divulgativo - Inserimento Tavole: Periodo Sinodico, Configurazione Pianeti Interni 

---

## Documentazione (PDF)
Tutti i documenti sono impaginati in $\LaTeX$ e consultabili nella cartella [`/pdf`](./pdf):

* **[Vicinato Cosmico — Articolo Divulgativo](<./pdf/Vicinato Cosmico - Articolo Divulgativo.pdf>)** — Introduzione, scale planetarie, periodo sinodico, risultati e limiti dei modelli.
* **[Formulazione Matematica — Orbite Circolari](<./pdf/Formulazione Matematica - Orbite Circolari.pdf>)** — Modello analitico semplificato e indice di vicinanza.
* **[Formulazione Matematica — Orbite Ellittiche](<./pdf/Formulazione Matematica - Orbite Ellittiche.pdf>)** — Estensione analitica al moto kepleriano.
* **[Equazione di Keplero](<./pdf/Equazione di Keplero.pdf>)** — Derivazione geometrica, anomalie.
* **[Metodo di Newton–Raphson](<./pdf/Metodo di Newton-Raphson.pdf>)** — Analisi della convergenza e verifica numerica..
* **[Analisi Codice — Orbite Circolari](<./pdf/Analisi Codice - Orbite Circolari.pdf>)** — Documentazione tecnica per orbite circolari.
* **[Analisi Codice — Orbite Ellittiche](<./pdf/Analisi Codice - Orbite Ellittiche.pdf>)** — Documentazione tecnica per orbite ellittiche.
* **[Codice Python — Orbite Circolari](<./pdf/Codice Python - Orbite Circolari.pdf>)** - Listato codice per calcolo percentuali (caso orbite circolari)
* **[Codice Python — Orbite Ellittiche](<./pdf/Codice Python - Orbite Ellittiche.pdf>)** - Listato codice per calcolo percentuali (caso orbite ellittiche)

---

## Codice e Dati
* [`/src`](./src): script Python eseguibili ([`percentuali_circolari.py`](./src/percentuali_circolari.py), [`percentuali_ellittiche.py`](./src/percentuali_ellittiche.py)).
* [`/data`](./data): tabelle dei risultati in formato CSV ([`percentuali_circolari.csv`](./data/percentuali_circolari.csv), [`percentuali_ellittiche.csv`](./data/percentuali_ellittiche.csv)).

### Esecuzione rapida
```bash
pip install -r requirements.txt
python src/percentuali_circolari.py
python src/percentuali_ellittiche.py
```
