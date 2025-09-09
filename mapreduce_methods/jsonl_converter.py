"""
jsonl文件转换器。

统一将各种格式的文件转换为jsonl文件。
"""

from __future__ import annotations

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class JsonlConverter:
    """
    基于pandas的jsonl转换器。
    """
    # ====暴露方法。====
    @staticmethod
    def auto_convert_and_save_jsonl(
        target_path: str | Path,
    ) -> pd.DataFrame:
        """
        自动识别文件类型，自动转换为jsonl文件。

        自动以相同文件名称但不同扩展名保存至同一文件夹下。

        Args:
            target_path (Union[str, Path]): 目标文件路径。

        Returns:
            pd.DataFrame: 读取的文件结果。一般可以不使用。
        """
        target_path = Path(target_path)
        result_path = target_path.with_suffix('.jsonl')
        return JsonlConverter.auto_convert_to_jsonl(
            target_path=target_path,
            result_path=result_path,
        )

    # ====暴露方法。====
    @staticmethod
    def auto_convert_to_jsonl(
        target_path: str | Path,
        result_path: str | Path,
    ) -> pd.DataFrame:
        """
        自动识别文件类型，自动转换为jsonl文件。

        Args:
            target_path (Union[str, Path]): 目标文件路径。
            result_path (Union[str, Path]): 结果文件指定保存的路径。

        Returns:
            pd.DataFrame: 读取的文件结果。一般可以不使用。
        """
        target_path = Path(target_path)
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        file_extension = target_path.suffix
        if file_extension == '.csv':
            return JsonlConverter.convert_csv_to_jsonl(
                target_path=target_path,
                result_path=result_path,
            )
        elif file_extension == '.xlsx':
            return JsonlConverter.convert_xlsx_to_jsonl(
                target_path=target_path,
                result_path=result_path,
            )

    # ====主要方法。====
    @staticmethod
    def convert_csv_to_jsonl(
        target_path: str | Path,
        result_path: str | Path,
    ) -> pd.DataFrame:
        """
        将csv文件转换为jsonl文件。

        Args:
            target_path (Union[str, Path]): 目标文件路径。
            result_path (Union[str, Path]): 结果文件指定保存的路径。

        Returns:
            pd.DataFrame: 读取的文件结果。一般可以不使用。
        """
        target_path = Path(target_path)
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        df = pd.read_csv(target_path)
        df.to_json(result_path.with_suffix('.jsonl'), orient='records', lines=True, force_ascii=False)
        print(f"Converted {target_path} to jsonl")
        return df

    # ====主要方法。====
    @staticmethod
    def convert_xlsx_to_jsonl(
        target_path: str | Path,
        result_path: str | Path,
    ) -> pd.DataFrame:
        """
        将xlsx文件转换为jsonl文件。

        Args:
            target_path (Union[str, Path]): 目标文件路径。
            result_path (Union[str, Path]): 结果文件指定保存的路径。

        Returns:
            pd.DataFrame: 读取的文件结果。一般可以不使用。
        """
        target_path = Path(target_path)
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        df = pd.read_excel(target_path)
        df.to_json(result_path.with_suffix('.jsonl'), orient='records', lines=True, force_ascii=False)
        print(f"Converted {target_path} to jsonl")
        return df

