import pandas as pd
import numpy as np


def fill_missing_median(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    
    for col in columns:
        if col in df.columns:
            median = df[col].median()
            df[col] = df[col].fillna(median)
    return df



def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    min_non_na = int((1 - threshold) * df.shape[1])
    return df.dropna(thresh=min_non_na)


def normalize_data(df, columns):
    df = df.copy()  # 避免链式赋值问题
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # 强制转数值
            min_val = df[col].min()
            max_val = df[col].max()
            if pd.notna(min_val) and pd.notna(max_val) and max_val > min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
    return df



def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:

    if series.std(ddof=0) == 0:
        return pd.Series(False, index=series.index)
    z_scores = (series - series.mean()) / series.std(ddof=0)
    return z_scores.abs() > threshold
