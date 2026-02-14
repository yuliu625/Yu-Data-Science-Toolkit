"""
基于pandas构建的map-reduce加速工具。

并不指定具体的文件格式。

但是后续这个包再没有后续进行更新，原因是:
    - 这个包的工具是基于面向对象的方式构建的，而我后来的工具类更多使用函数式编程的方式。
    - 对于处理大型文件，pandas很糟糕。
    - 我约定使用jsonline文件，构建针对性的工具，从而更好地面对各种情况。
"""

__all__ = [
    'DfAccelerator',
    'BaseDfSplitter',
    'BaseDFConcater'
]

from .df_accelerator import DfAccelerator
from .df_splitter import BaseDfSplitter
from .df_concater import BaseDFConcater

