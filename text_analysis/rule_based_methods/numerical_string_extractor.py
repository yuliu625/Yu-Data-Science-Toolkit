"""
基于正则方法提取文本中进行数值计算的部分。
"""

from __future__ import annotations

import re

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class NumericalStringExtractor:
    @staticmethod
    def extract_numerical_strings(
        text: str,
    ) -> list[str]:
        """
        提取一段字符串中属于数值的部分。

        Args:
            text (str): 原始字符串。

        Returns:
            list[str]: 作为字符串的数值列表。
        """
        # 这个模式可以匹配整数、浮点数、带逗号的数字、负数和科学计数法。
        pattern = r'[-+]?[\d,]+(?:\.\d+)?(?:[eE][-+]?\d+)?'
        matches = re.findall(pattern, text)
        return matches

    @staticmethod
    def calculate_numerical_string_length(
        text: str,
    ) -> int:
        """
        计算含有实际为数字的字符串的数量。

        Args:
            text (str): 原始字符串。

        Returns:
            int: 作为字符串的数值数量。
        """
        return len(NumericalStringExtractor.extract_numerical_strings(text))

    @staticmethod
    def calculate_numerical_char_length(
        text: str,
    ) -> int:
        """
        计算含有实际为数字的字符串的长度累计。

        Args:
            text (str): 原始字符串。

        Returns:
            int: 作为字符串的数值的长度累计。
        """
        count = 0
        numerical_strings = NumericalStringExtractor.extract_numerical_strings(text)
        for numerical_string in numerical_strings:
            count += len(numerical_string)
        return count

