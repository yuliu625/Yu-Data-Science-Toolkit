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
    def concat_dfs_by_directory(self, *args, **kwargs) -> pd.DataFrame:
        """主要方法，聚合一个文件夹下的df。"""

    @abstractmethod
    def read_a_df(self, df_path: str | Path) -> pd.DataFrame:
        """读取一个df的方法。"""

    @abstractmethod
    def save_a_df(self, df: pd.DataFrame, path_to_save: str | Path) -> None:
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

    def run(self, **kwargs):
        """
        主要方法。
        """
        # 进行合并。
        result_df = self.concat_dfs_by_directory(self.target_dir)
        # 保存结果。
        self.save_a_df(result_df, self.path_to_save)
        # 打印提示。
        print(f"合并完成，保存至{str(self.path_to_save)}")

    def concat_dfs_by_directory(
        self,
        target_dir: Annotated[str | Path, "需要进行连接的文件夹目录。"],
    ) -> pd.DataFrame:
        """
        合并一个dir中所有的df。

        Args:
            target_dir: target_dir: 需要进行连接的文件夹目录。
        Return:
            合并后的df。
        """
        # pipeline
        # 获取待处理df路径。
        df_path_list = self.get_df_path_list(target_dir)
        # 读取df。
        df_list = self._get_df_list(df_path_list)
        # 执行合并。
        result_df = self.concat_df(df_list)
        return result_df

    def _get_df_list(
        self,
        df_path_list: list[Path],
    ) -> list[pd.DataFrame]:
        """
        获得当前文件夹下所有的df，会使用需要实现的读取df文件的方法。

        Args:
            df_path_list: 待合并的df路径的列表。默认是类中方法get_df_path_list返回的结果。
        Return:
            list[pd.DataFrame], 一个列表，内容是所有的df。
        """
        # 使用interface中的读取df的方法，批量读取df。
        df_list = [
            self.read_a_df(df_path) for df_path in df_path_list
        ]
        return df_list

    def get_df_path_list(
        self,
        target_dir: Annotated[str | Path, "需要进行连接的文件夹目录。"]
    ) -> list[Path]:
        """
        遍历当前的文件夹，获取所有是文件的文件路径。

        Args:
            target_dir: 需要进行连接的文件夹目录。
        Return:
            list[Path], 一个列表，内容是所有的df的路径。
        """
        target_dir = Path(target_dir)  # 冗余构建Path对象，确保可是正常使用Path相关方法。
        # 检索一个文件夹下所有的文件，记录为待处理的df的路径。
        df_path_list = [df_path for df_path in target_dir.iterdir() if df_path.is_file()]
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

    def read_a_df(self, df_path: str | Path) -> pd.DataFrame:
        ...

    def save_a_df(self, df: pd.DataFrame, path_to_save: str | Path) -> None:
        ...


def _test_df_concater():
    df_concater = DefaultDFConcater(
        target_dir=r'/path/to/dir',
        path_to_save=r'/path/to/save',
    )
    df_concater.run()


if __name__ == '__main__':
    _test_df_concater()
