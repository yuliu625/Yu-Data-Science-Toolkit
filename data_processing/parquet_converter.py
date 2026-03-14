"""
Sources:
    https://github.com/yuliu625/Yu-Data-Science-Toolkit/data_processing/parquet_converter.py

References:
    None

Synopsis:
    将原始数据文件转换为 parquet 文件的转换器。

Notes:
    这个仓库的中心数据表示方法。
    polars 相比 pandas 足够好用，parquet 的转换一劳永逸。当前方法为通用脚本，具体情况可以自行实现转换方法。

    parquet 具有的优势有:
        - apache arrow 体系: 这里省略 arrow 体系的特性。
        - schema: parquet 为自描述格式，一次人工 schema 定义，后续均为精确解析。

    约定:
        - 统一表示: 这个仓库的后续结构化数据处理均由 polars 进行处理。
        - 统一持久化: 各种数据格式均以 parquet 进行处理。

    场景:
        - 其他数据库: 老旧或不支持直接连接数据库，通过规范 schema description 文件自行转换。
        - 流式数据转分析数据: 从 jsonl 或 avro 数据转换，用于支持 apache arrow 体系执行分析。
"""

from __future__ import annotations
from loguru import logger

import polars as pl
from pathlib import Path

from typing import TYPE_CHECKING, Mapping
# if TYPE_CHECKING:


class ParquetConverter:
    """
    基于 polars 的 parquet 转换器。
    """
    @staticmethod
    def convert_and_save_parquet(
        target_path: str | Path,
        result_path: str | Path,
    ):
        # path processing
        target_path = Path(target_path)
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def convert_and_save_parquet_from_jsonl(
        target_path: str | Path,
        schema_overrides: Mapping[str, pl.DataType],
        result_path: str | Path,
    ) -> None:
        raise NotImplementedError

    @staticmethod
    def convert_and_save_parquet_from_avro(
        target_path: str | Path,
        schema_overrides: Mapping[str, pl.DataType],
        result_path: str | Path,
    ) -> None:
        raise NotImplementedError

    @staticmethod
    def convert_and_save_parquet_from_json(
        target_path: str | Path,
        schema_overrides: Mapping[str, pl.DataType],
        result_path: str | Path,
    ) -> None:
        df = pl.read_json(
            source=target_path,
            schema=schema_overrides,
        )
        logger.trace(f"\ndf: \n{df}")
        df.write_parquet(
            result_path,
        )
        logger.success(f"Saved parquet file to {result_path}")

    @staticmethod
    def convert_and_save_parquet_from_csv(
        target_path: str | Path,
        schema_overrides: Mapping[str, pl.DataType],
        result_path: str | Path,
    ) -> None:
        raise NotImplementedError

    @staticmethod
    def convert_and_save_parquet_from_xlsx(
        target_path: str | Path,
        schema_overrides: Mapping[str, pl.DataType],
        result_path: str | Path,
    ) -> None:
        raise NotImplementedError



