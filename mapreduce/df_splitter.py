"""
df分割器。

将一个df按行分解为多个相同结构的df，并保存。
有些时候一些df过大，因此就需要将其分解为多个df，然后并行执行操作。
"""

import pandas as pd
from pathlib import Path

from abc import ABC, abstractmethod
from typing import Annotated


class DfSplitterInterface(ABC):
    """
    df分割器。

    将一个df分割为多个df，结果保存在一个指定文件夹下。
    """
    @abstractmethod
    def split_df(self, *args, **kwargs) -> list[pd.DataFrame]:
        """分割一个df。"""

    @abstractmethod
    def read_a_df(self, df_path: str | Path) -> pd.DataFrame:
        """读取一个df的方法。"""

    @abstractmethod
    def save_a_df(self, df: pd.DataFrame, path_to_save: str | Path) -> None:
        """保存最终df的方法。"""


class BaseDfSplitter(DfSplitterInterface):
    def __init__(
        self,
        target_df_path: Annotated[str | Path, "需要进行连接的文件夹目录。"],
        dir_to_save: Annotated[str | Path, "保存结果的文件目录。"],
    ):
        self.target_df_path = Path(target_df_path)
        self.dir_to_save = Path(dir_to_save)

    def run(self, **kwargs):
        """
        主要方法。
        """

    def split_df(
        self,
        df: pd.DataFrame,
        num_splits: int
    ) -> list[pd.DataFrame]:
        chunk_size = len(df) // num_splits + 1
        chunks = []
        for i in range(num_splits + 1):
            start = i * chunk_size
            end = None if i == chunk_size - 1 else (i + 1) * chunk_size
            chunks.append(df[start:end])

        return chunks

    def get_file_names_list(self) -> list[str]:
        ...


class DefaultDfSplitter(BaseDfSplitter):
    def __init__(
        self,
        target_df_path: Annotated[str | Path, "需要进行连接的文件夹目录。"],
        dir_to_save: Annotated[str | Path, "保存结果的文件目录。"]
    ):
        super().__init__(target_df_path, dir_to_save)

    def read_a_df(self, df_path: str | Path) -> pd.DataFrame:
        ...

    def save_a_df(self, df: pd.DataFrame, path_to_save: str | Path) -> None:
        ...


if __name__ == '__main__':
    pass
