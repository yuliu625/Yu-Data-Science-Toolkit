"""

"""

from .df_splitter import DefaultDfSplitter
from .df_concater import DefaultDFConcater

from pathlib import Path
from typing import Callable, Annotated, Any

from abc import ABC, abstractmethod

import asyncio


class DfAcceleratorInterface(ABC):
    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        """加速运行某个方法。"""


class DfAccelerator:
    def __init__(
        self,
        target_df_path: Annotated[str | Path, "需要进行连接的文件夹目录。"],
        dir_to_save: Annotated[str | Path, "保存结果的文件目录。"],
        num_splits: Annotated[int, "指定的切片的数量。"],
        read_a_df_func: Callable,
        save_a_df_func: Callable,
    ):
        self.df_splitter = DefaultDfSplitter(
            target_df_path=target_df_path,
            dir_to_save=dir_to_save,
            num_splits=num_splits,
        )
        self.df_concater = DefaultDFConcater(
            target_dir=dir_to_save,
            path_to_save=dir_to_save / r"result.txt",
        )
        setattr(self.df_splitter, 'save_a_df', save_a_df_func)
        setattr(self.df_concater, 'save_a_df', save_a_df_func)
        setattr(self.df_splitter, 'read_a_df', read_a_df_func)
        setattr(self.df_concater, 'read_a_df', read_a_df_func)


if __name__ == '__main__':
    pass
