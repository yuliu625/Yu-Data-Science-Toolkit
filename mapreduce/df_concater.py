

import pandas as pd
from pathlib import Path

from abc import ABC, abstractmethod

from typing import Annotated


class DFConcaterInterface(ABC):
    @abstractmethod
    def concat_df_by_directory(self, *args, **kwargs) -> pd.DataFrame:
        """主要方法，聚合所有df。"""

    @abstractmethod
    def get_a_df(self, df_path: str | Path) -> pd.DataFrame:
        """读取一个df的方法。"""

    @abstractmethod
    def save_result(self, *args, **kwargs):
        """保存最终df的方法。"""


class BaseDFConcater(DFConcaterInterface):
    def __init__(
        self,
        target_dir: Annotated[str | Path, "需要进行连接的文件夹目录。"],
        path_to_save: Annotated[str | Path, "保存结果的文件目录。"],
    ):
        self.target_dir = Path(target_dir)
        self.path_to_save = Path(path_to_save)

    def concat_df_by_directory(self, *args, **kwargs) -> pd.DataFrame:
        """

        :param args:
        :param kwargs:
        :return:
        """
        df_list = self._get_df_list()
        result = pd.concat(df_list, **kwargs)
        return result

    def _get_df_list(self) -> list[pd.DataFrame]:
        """
        获得当前文件夹下所有的df，会使用需要实现的读取df文件的方法。

        Return:
            list[pd.DataFrame], 一个列表，内容是所有的df。
        """
        df_path_list = self._get_df_path_list()
        df_list = [
            self.get_a_df(df_path) for df_path in df_path_list
        ]
        return df_list

    def _get_df_path_list(self) -> list[Path]:
        """
        遍历当前的文件夹，获取所有是文件的文件路径。

        Return:
            list[Path], 一个列表，内容是所有的df的路径。
        """
        df_path_list = [df_path for df_path in self.target_dir.iterdir() if df_path.is_file()]
        return df_path_list


if __name__ == '__main__':
    pass
