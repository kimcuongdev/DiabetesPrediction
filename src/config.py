import os
from pathlib import Path

# Gốc của project (giả sử file config.py nằm trong src/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Đường dẫn dữ liệu
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA = DATA_DIR / "raw" / "diabetes.csv"
PROCESSED_DATA_DIR = DATA_DIR / "processed" 

# Đường dẫn mô hình
MODELS_DIR = PROJECT_ROOT / "models"
MODEL_FILE = MODELS_DIR / "diabetes_model.pkl"

# Đường dẫn output
OUTPUT_DIR = PROJECT_ROOT / "outputs"
