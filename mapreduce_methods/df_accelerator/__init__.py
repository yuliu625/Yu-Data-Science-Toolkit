"""
基于pandas构建的map-reduce加速工具。

并不指定具体的文件格式。
"""

__all__ = [
    'DfAccelerator',
    'BaseDfSplitter',
    'BaseDFConcater'
]

from .df_accelerator import DfAccelerator
from .df_splitter import BaseDfSplitter
from .df_concater import BaseDFConcater

