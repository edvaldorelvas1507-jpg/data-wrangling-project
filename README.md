# Auditoría de Carbono Corporativa: Evaluando la Huella Ecológica en el Sector Tecnológico

Proyecto final del Módulo 1 (procesamiento y recuperación de datos) del bootcamp de Análisis de Datos de Ironhack.

Equipo: Edvaldo Relvas Jr (recolección y limpieza de datos), Iván y Alejandro. Entrega: 14 de noviembre de 2026.

## Introducción
Analizamos cuánto emiten tres grandes tecnológicas (Apple, Amazon y Microsoft) y cómo se reparte su huella de carbono entre los Scopes 1, 2 y 3, comparándola con sus ingresos.

## Datos y fuentes
- Emisiones (Scope 1, Scope 2 location-based y market-based, Scope 3): informes de sostenibilidad de cada empresa.
  - Amazon: Sustainability Report 2024 (tablas accesibles).
  - Microsoft: Environmental Data Fact Sheet 2025.
  - Apple: Environmental Progress Reports (2022, 2024 y 2025) y CDP 2022.
- Ingresos: informes anuales de las empresas (pendiente de verificar en los 10-K).
- Web scraping: Wikipedia, "List of largest technology companies by revenue" (notebook `notebooks/scraping_wikipedia.ipynb`). Se usa para contrastar ingresos; no incluye Amazon ni emisiones.

Los datos no se suben a GitHub (la carpeta `data/` está en `.gitignore`). No inventamos valores: cada empresa se muestra con los años que tiene publicados.

## Preguntas de investigación (hipótesis)
1. Evolución: las emisiones totales de las empresas han aumentado con los años.
2. Peso del Scope 3: la mayor parte de la huella está en el Scope 3, no en los Scopes 1 y 2.
3. Scope 2: comprar energía renovable reduce mucho el Scope 2 declarado (diferencia entre location-based y market-based).

## Metodología
Periodo común 2020–2022, más las tendencias individuales hasta el último año de cada empresa. Recolección de tablas (PDF, Excel, web scraping), limpieza con pandas, dataset consolidado, análisis y visualización.

## Estructura del repositorio
- `notebooks/`: notebooks de trabajo (`main.ipynb`, `scraping_wikipedia.ipynb`).
- `src/`: funciones reutilizables (`collection.py`, `cleaning.py`, `analysis.py`, `config.py`).
- `data/raw/` y `data/clean/`: datos originales y limpios (solo en local).

## Principales hallazgos
(Pendiente.)

## Próximos pasos
(Pendiente.)

## Enlaces
- Tablero Kanban (Trello): https://trello.com/b/iI48iMSO/proyecto-emisiones-tecnol%C3%B3gicas
