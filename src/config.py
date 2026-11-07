"""Constantes del proyecto (rutas, empresas, anios). Sin valores sueltos en el codigo."""
from pathlib import Path

RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")

COMPANIES = ["Apple", "Amazon", "Microsoft"]
COMMON_YEARS = [2020, 2021, 2022]
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue"
