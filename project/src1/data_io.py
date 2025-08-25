import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")

# 确保目录存在
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

def save_raw_data(df: pd.DataFrame, filename: str):
    """保存原始数据为 CSV"""
    filepath = RAW_DATA_DIR / filename
    df.to_csv(filepath, index=False)
    print(f"[save_raw_data] Saved to {filepath.resolve()}")

def save_processed_data(df: pd.DataFrame, filename: str):
    """保存处理后数据为 Parquet"""
    filepath = PROCESSED_DATA_DIR / filename
    df.to_parquet(filepath, index=False)
    print(f"[save_processed_data] Saved to {filepath.resolve()}")

def load_raw_data(filename: str) -> pd.DataFrame:
    """加载原始 CSV 数据"""
    filepath = RAW_DATA_DIR / filename
    df = pd.read_csv(filepath)
    print(f"[load_raw_data] Loaded from {filepath.resolve()}")
    return df

def load_processed_data(filename: str) -> pd.DataFrame:
    """加载处理后 Parquet 数据"""
    filepath = PROCESSED_DATA_DIR / filename
    df = pd.read_parquet(filepath)
    print(f"[load_processed_data] Loaded from {filepath.resolve()}")
    return df
