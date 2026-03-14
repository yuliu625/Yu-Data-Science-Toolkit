"""
Sources:
    https://github.com/yuliu625/Yu-Data-Science-Toolkit/data_processing/parquet_converter.py

References:
    None

Synopsis:
    将原始数据文件转换为 parquet 文件的转换器。

Notes:
    这个仓库的中心数据表示方法。

    parquet 具有的优势有:
        - apache arrow 体系: 这里省略 arrow 体系的特性。
        - schema: parquet 为自描述格式，一次人工 schema 定义，后续均为精确解析。

    约定:
        - 统一表示: 这个仓库的后续结构化数据处理均由 polars 进行处理。
        - 统一持久化: 各种数据格式均以 parquet 进行处理。
"""

from __future__ import annotations
from loguru import logger

import polars as pl
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ParquetConverter:
    ...

