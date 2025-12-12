# src/config.py
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]  # project root
RAW_DIR = BASE / "data_raw"
CLEAN_DIR = BASE / "data_clean"
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

CLEAN_FILE = CLEAN_DIR / "clean_data.csv"
TIME_INTERVAL = "1T"  # 1 minute; change to "30S" or "5T" if desired
