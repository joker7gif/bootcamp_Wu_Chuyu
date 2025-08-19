# 让 src 目录被识别为一个 Python 包
# 这样可以使用 from src import cleaning

# 可选择性导入常用模块或函数（方便使用）
from . import cleaning

# 如果需要直接通过 from src import * 来用函数，可以加：
# from .cleaning import fill_missing_median, drop_missing, normalize_data, detect_outliers_zscore

__all__ = [
    "cleaning",
]
