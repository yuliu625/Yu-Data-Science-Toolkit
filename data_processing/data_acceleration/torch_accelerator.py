"""
基于torch中的dataset和dataloader构建的加速处理工具。

这个工具的构建是以通用目的进行的，相比于直接使用多线程和使用异步编程，可能有些舍近求远。

使用pytorch中的dataset和dataloader实现多线程。
"""

from __future__ import annotations

import torch

from typing import TYPE_CHECKING
# if TYPE_CHECKING:
