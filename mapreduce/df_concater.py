"""
df合并器。

这是一个脆弱的方法，默认会和df_splitter一起使用。
不过默认场景下，依然可以合并一个文件夹下所有相关结构的df。
"""

import pandas as pd
from pathlib import Path

from abc import ABC, abstractmethod
from typing import Annotated


class DFConcaterInterface(ABC):
    """
    df合并器。

    将一个文件夹下所有的df合并为一个df，并将结果保存到指定路径。
    """
    @abstractmethod
    def concat_df_by_directory(self, *args, **kwargs) -> pd.DataFrame:
        """主要方法，聚合一个文件夹下的df。"""

    @abstractmethod
    def get_a_df(self, df_path: str | Path) -> pd.DataFrame:
        """读取一个df的方法。"""

    @abstractmethod
    def save_result(self, df: pd.DataFrame) -> None:
        """保存最终df的方法。"""


class BaseDFConcater(DFConcaterInterface):
    """
    基础的合并df的工具类。
    并不指定具体的df类型。

    可能需要重写的方法:
        - get_df_path_list。获得df_path的方法。默认实现是直接去搜索当前文件夹下所有的文件，仅排除文件夹。可以进行的重写:
            - 通过扩展名，选择某种文件格式的df。
            - 递归搜索，搜索指定文件树深度或者全部的df。
        - concat_df。合并df的方法。默认实现使用pandas的concat方法。可以进行的修改:
            - 指定pd.concat的kwargs。
            - 增加更多的限制，以其他方式或其他顺序连接。（但也可以对合并结果进行处理，而不是在这里重写。）
    """
    def __init__(
        self,
        target_dir: Annotated[str | Path, "需要进行连接的文件夹目录。"],
        path_to_save: Annotated[str | Path, "保存结果的文件目录。"],
    ):
        self.target_dir = Path(target_dir)
        self.path_to_save = Path(path_to_save)

    def run(self):
        """
        主要方法。
        """
        result_df = self.concat_df_by_directory()
        self.save_result(result_df)

    def concat_df_by_directory(self) -> pd.DataFrame:
        """
        合并一个dir中所有的df。

        Return:
            合并后的df。
        """
        df_list = self._get_df_list()
        result_df = self.concat_df(df_list)
        return result_df

    def _get_df_list(self) -> list[pd.DataFrame]:
        """
        获得当前文件夹下所有的df，会使用需要实现的读取df文件的方法。

        Return:
            list[pd.DataFrame], 一个列表，内容是所有的df。
        """
        df_path_list = self.get_df_path_list()
        df_list = [
            self.get_a_df(df_path) for df_path in df_path_list
        ]
        return df_list

    def get_df_path_list(self) -> list[Path]:
        """
        遍历当前的文件夹，获取所有是文件的文件路径。

        Return:
            list[Path], 一个列表，内容是所有的df的路径。
        """
        df_path_list = [df_path for df_path in self.target_dir.iterdir() if df_path.is_file()]
        return df_path_list
    
    def concat_df(self, df_list: list[pd.DataFrame]) -> pd.DataFrame:
        """
        合并给出dfs。
        
        Args:
            df_list: 以列表形式给出的df。
        Return: 
            合并后的结果。
        """
        return pd.concat(df_list, ignore_index=True)


class DefaultDFConcater(BaseDFConcater):
    """
    默认继承BaseDFConcater的方法。

    需要实现必要的2个读写方法。
    之后仅使用run方法就可以完成全部操作。
    """
    def __init__(
        self, 
        target_dir: Annotated[str | Path, "需要进行连接的文件夹目录。"],
        path_to_save: Annotated[str | Path, "保存结果的文件目录。"]
    ):
        super().__init__(target_dir, path_to_save)

    def get_a_df(self, df_path: str | Path) -> pd.DataFrame:
        ...

    def save_result(self, df: pd.DataFrame) -> None:
        ...


def _test_df_concater():
    df_concater = DefaultDFConcater(
        target_dir=r'/path/to/dir',
        path_to_save=r'/path/to/save',
    )
    df_concater.run()


if __name__ == '__main__':
    _test_df_concater()
