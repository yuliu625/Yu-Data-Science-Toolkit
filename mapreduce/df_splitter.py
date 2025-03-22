"""
将一个df按行分解为多个相同结构的df，并保存。

有些时候一些df过大，因此就需要将其分解为多个df，然后并行执行操作。
"""

from abc import ABC, abstractmethod

import pandas as pd

from pathlib import Path


class DfSplitter(ABC):
    """
    通用的df分解类，这个抽象类需要实现：
        - 加载df。原本的数据可能为多种结构，并且具体的字段需要指定加载方式。
        - 保存df。指定保存结构，以及保存位置。
    """
    @abstractmethod
    def get_df(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def save_df(self) -> None:
        pass

    def split_df(self) -> pd.DataFrame:
        pass


if __name__ == '__main__':
    pass
