import pandas as pd
import numpy as np


def fill_missing_median(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    用中位数填补指定列中的缺失值（NaN），不修改为0的值
    """
    for col in columns:
        if col in df.columns:
            median = df[col].median()
            df[col] = df[col].fillna(median)
    return df



def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    删除缺失比例大于阈值的行
    threshold = 0.5 表示：缺失值超过50%则删除该行
    """
    # thresh 是非缺失值最少数量
    min_non_na = int((1 - threshold) * df.shape[1])
    return df.dropna(thresh=min_non_na)


def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    对指定列做 0-1 归一化
    """
    for col in columns:
        if col in df.columns:
            min_val = df[col].min()
            max_val = df[col].max()
            if pd.notna(min_val) and pd.notna(max_val) and max_val > min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
    return df


def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """
    返回布尔掩码：True 表示 |z-score| > threshold
    """
    if series.std(ddof=0) == 0:
        return pd.Series(False, index=series.index)
    z_scores = (series - series.mean()) / series.std(ddof=0)
    return z_scores.abs() > threshold
