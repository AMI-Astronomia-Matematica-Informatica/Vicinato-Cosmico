# Vicinato Cosmico
**Analisi geometrica e temporale delle distanze nel Sistema Solare**

Progetto del laboratorio digitale **AMI** (*Astronomia, Matematica, Informatica*) — a cura di **Massimiliano Santini**.

---

## Panoramica
Analizzando la dinamica orbitale lungo un intero periodo sinodico Urano–Nettuno (**171 anni**, 62.607 giorni), il progetto dimostra come **Mercurio** sia in media il pianeta più vicino non solo alla Terra, ma a ciascuno degli altri pianeti del Sistema Solare.

---

## Documentazione (PDF)
Tutti i documenti sono impaginati in $\LaTeX$ e consultabili nella cartella [`/pdf`](./pdf):

* **[Vicinato Cosmico — Articolo Divulgativo](<./pdf/Vicinato Cosmico - Articolo Divulgativo.pdf>)** — Introduzione, scale planetarie, periodo sinodico, limiti dei modelli e risultati.
* **[Formulazione Matematica — Orbite Circolari](<./pdf/Formulazione Matematica - Orbite Circolari.pdf>)** — Modello analitico semplificato e indice di vicinanza.
* **[Formulazione Matematica — Orbite Ellittiche](<./pdf/Formulazione Matematica - Orbite Ellittiche.pdf>)** — Estensione analitica al moto kepleriano.
* **[Equazione di Keplero](<./pdf/Equazione di Keplero.pdf>)** — Derivazione geometrica, anomalie e teorema di esistenza e unicità.
* **[Metodo di Newton–Raphson](<./pdf/Metodo di Newton-Raphson.pdf>)** — Analisi della convergenza quadratica e verifica numerica (`float64`).
* **[Analisi Codice — Orbite Circolari](<./pdf/Analisi Codice - Orbite Circolari.pdf>)** — Documentazione tecnica e complessità computazionale.
* **[Analisi Codice — Orbite Ellittiche](<./pdf/Analisi Codice - Orbite Ellittiche.pdf>)** — Documentazione del risolutore vettoriale e confronto tra gli algoritmi.
* **[Codice Python — Orbite Circolari](<./pdf/Codice Python - Orbite Circolari.pdf>)** & **[Codice Python — Orbite Ellittiche](<./pdf/Codice Python - Orbite Ellittiche.pdf>)** — Listati sorgente completi.

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
