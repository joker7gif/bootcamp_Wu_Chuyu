import pandas as pd

def fill_missing_median(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Fill missing values with median for specified columns."""
    for col in cols:
        if col in df.columns:
            median = df[col].median()
            df[col] = df[col].fillna(median)
            print(f"[fill_missing_median] Filled {col} with median={median:.2f}")
    return df

def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Drop columns with missing value proportion above threshold."""
    missing_ratio = df.isnull().mean()
    drop_cols = missing_ratio[missing_ratio > threshold].index
    df = df.drop(columns=drop_cols)
    print(f"[drop_missing] Dropped columns: {list(drop_cols)}")
    return df

def normalize_data(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Min-max normalize specified columns to [0,1]."""
    for col in cols:
        if col in df.columns:
            min_val, max_val = df[col].min(), df[col].max()
            if max_val > min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
                print(f"[normalize_data] Normalized {col}")
    return df

def remove_outliers_iqr(df: pd.DataFrame, cols: list, k: float = 1.5) -> pd.DataFrame:
    """Remove outliers using IQR method for specified columns."""
    for col in cols:
        if col in df.columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - k * iqr
            upper = q3 + k * iqr
            before = len(df)
            df = df[(df[col] >= lower) & (df[col] <= upper)]
            after = len(df)
            print(f"[remove_outliers_iqr] {col}: removed {before-after} rows")
    return df
