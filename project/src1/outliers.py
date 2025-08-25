# src1/outliers.py
import pandas as pd

def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """
    Detect outliers using the IQR method.
    Returns a boolean mask where True indicates an outlier.
    k: multiplier for IQR (default 1.5 for standard definition)
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return (series < lower) | (series > upper)

def remove_outliers_iqr(df: pd.DataFrame, columns: list[str], k: float = 1.5) -> pd.DataFrame:
    """
    Remove rows that contain outliers in any of the given columns.
    """
    mask = pd.Series(False, index=df.index)
    for col in columns:
        mask |= detect_outliers_iqr(df[col], k)
    return df[~mask].copy()
