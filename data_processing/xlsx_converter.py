"""
Sources:
    https://github.com/yuliu625/Yu-Data-Science-Toolkit/data_processing/xlsx_converter.py

References:
    None

Synopsis:
    将原始数据文件转换为 xlsx 文件的转换器。

Notes:
    xlsx 并不是这个仓库设计的中心数据格式，但是:
        - 易于操作: 将数据转换为 xlsx 形式发送给其他协作者，其他协作者可以通过 excel 打开和查看文件。
        - 论文制图: 少数情况下，结果由自动化生成，不经过处理直接自动化生成 latex 表格。
    这些情况下，将 df 转换为 xlsx文件。

    xlsx 不应该作为数据计算和处理的中心，仅仅是为了向其他人展示结果。
    因此，仅包含单向转换方法。

    需要:
        - 读取: fastexcel
        - 写入: xlsxwriter
"""

from __future__ import annotations
from loguru import logger

import polars as pl
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class XlsxConverter:
    """
    基于 polars 的 xlsx 文件转换器。
    """
    @staticmethod
    def convert_and_save_xlsx(
        df: pl.DataFrame,
        result_path: str | Path,
    ) -> None:
        """
        转换和保存 xlsx 文件。

        约定:
            - 基于精确文件转换: 已经基于 polars 有更精确的表示，从已加载的内存中进行转换。
            - 为展示保存: 保存的目的是为了向他人展示，直接对数据进行保存。

        Args:
            df (pl.DataFrame): 已经加载的基于 polars 的数据。
            result_path (Union[str, Path]): 结果保存路径。
                约定扩展名为 .xlsx，会自动处理中间路径的文件夹。

        Returns:
            None: 保存结果。不对报错进行处理，成功会以日志进行输出。
        """
        # path processing
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        # save as xlsx
        df.write_excel(result_path)
        logger.success(f"Saved {result_path}")

