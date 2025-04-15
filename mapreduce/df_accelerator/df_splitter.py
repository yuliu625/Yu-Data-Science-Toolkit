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
    """
    基础的分割df的工具类。
    并不指定具体的df类型。

    可能需要重写的方法:
        - get_file_names_list。指定保存文件的名字。默认以数字命名，并指定扩展名为.txt。可以进行的重写:
            - 指定扩展名。方便之后读取。
            - 其他命名方式。不仅仅是数字。
            但是默认分割是中间过程，因此可以不修改。
    """
    def __init__(
        self,
        target_df_path: Annotated[str | Path, "需要进行连接的文件夹目录。"],
        dir_to_save: Annotated[str | Path, "保存结果的文件目录。"],
        num_splits: Annotated[int, "指定的切片的数量。"],
    ):
        self.target_df_path = Path(target_df_path)
        self.dir_to_save = Path(dir_to_save)
        self.num_splits = num_splits

        # 冗余性检查，保存路径需要存在。
        self.dir_to_save.mkdir(parents=True, exist_ok=True)

    def run(self, **kwargs):
        """
        主要方法。
        """
        # 读取待处理df
        target_df = self.read_a_df(self.target_df_path)
        # 分割df。
        df_list = self.split_df(target_df, self.num_splits)
        # 获取文件名。
        file_names_list = self.get_file_names_list(self.num_splits)
        # 获取df的存储路径。
        path_to_save_list = self._get_path_to_save_list(file_names_list, self.dir_to_save)
        # 将所有df保存到对应指定的位置。
        self._batch_save_dfs(df_list, path_to_save_list)
        print(f"分割完成，保存至{str(self.dir_to_save)}，分割为{self.num_splits}块。")

    def split_df(
        self,
        df: Annotated[pd.DataFrame, "待被分割的df。"],
        num_splits: Annotated[int, "指定的切片的数量。"],
    ) -> list[pd.DataFrame]:
        """
        将一个df分割为指定块数。
        如果不能恰好分割（常见情况），则大小相近，最后一块会小一些。

        Args:
            df: 待被分割的df。
            num_splits: 指定的切片的数量。

        Returns:
            一个列表，其中的元素为已经按顺序做好的切片。
        """
        # 计算每个分割块的长度，向上取整，保证不遗漏，又大小近似。
        chunk_size = len(df) // num_splits + 1
        # 进行划分。
        chunks = []
        for i in range(num_splits):  # 构建指定数量的切片。
            start = i * chunk_size  # 起始位置从正常index开始。
            end = (i + 1) * chunk_size - 1  # 结束位置由下一index开始，-1不重叠。
            chunks.append(df[start:end])  # pandas会自动处理超界index。
        return chunks

    def get_file_names_list(
        self,
        num_splits: Annotated[int, "指定的切片的数量。"],
    ) -> list[str]:
        """
        获得待存储df的文件名列表。

        Args:
            num_splits: 指定的切片的数量。

        Returns:
            待存储df的文件名，以list按顺序存储。
        """
        return [f"{i}.txt" for i in range(num_splits)]

    def _get_path_to_save_list(
        self,
        file_names_list: list[str],
        dir_to_save: Path,
    ) -> list[Path]:
        """
        由文件名列表，批量获得df存储路径列表。
        这个方法配合get_file_names_list使用。

        Args:
            file_names_list: 文件的名字的列表。
            dir_to_save: 保存文件的文件夹路径。

        Returns:
            文件路径的列表。
        """
        return [
            self._get_path_to_save(file_name, dir_to_save)
            for file_name in file_names_list
        ]

    def _get_path_to_save(
        self,
        file_name: str,
        dir_to_save: Path,
    ) -> Path:
        """
        由文件名，获得df存储路径。
        这个方法是_get_path_to_save_list使用的方法。

        Args:
            file_name: 文件的名字。
            dir_to_save: 保存文件的文件夹路径。

        Returns:
            文件完整路径。默认使用pathlib实现。
        """
        return dir_to_save / file_name

    def _batch_save_dfs(
        self,
        df_list: list[pd.DataFrame],
        path_to_save_list: list[Path],
    ) -> None:
        """
        将df的列表批量存储到对应的指定位置。

        Args:
            df_list:
            path_to_save_list:
        """
        for i in range(len(df_list)):
            self.save_a_df(df_list[i], path_to_save_list[i])


class DefaultDfSplitter(BaseDfSplitter):
    def __init__(
        self,
        target_df_path: Annotated[str | Path, "需要进行连接的文件夹目录。"],
        dir_to_save: Annotated[str | Path, "保存结果的文件目录。"],
        num_splits: Annotated[int, "指定的切片的数量。"],
    ):
        super().__init__(target_df_path, dir_to_save, num_splits)

    def read_a_df(self, df_path: str | Path) -> pd.DataFrame:
        ...

    def save_a_df(self, df: pd.DataFrame, path_to_save: str | Path) -> None:
        ...

    # def get_file_names_list(self, num_splits: int) -> list[str]:
    #     ...


def _test_df_splitter():
    df_splitter = DefaultDfSplitter(
        target_df_path=r'/path/to/df',
        dir_to_save=r'/path/to/save',
        num_splits=3,
    )
    df_splitter.run()


if __name__ == '__main__':
    _test_df_splitter()
