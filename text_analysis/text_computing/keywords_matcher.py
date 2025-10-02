"""
使用keywords对于文本进行规则匹配。
"""

from __future__ import annotations

import re

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class KeywordsMatcher:
    @staticmethod
    def calculate_matched_keywords_number(
        text: str,
        keywords: list[str],
    ) -> int:
        """
        计算所有keywords的命中数量。

        可以构建中间方法，计算每一个keywords的命中数量。

        Args:
            text (str): 原始文本。
            keywords (list[str]): 需要匹配的多个keywords。

        Returns:
            int: 命中所有keywords的总计数。
        """
        keywords_matches = KeywordsMatcher.match_keywords(
            text=text,
            keywords=keywords,
        )
        keywords_numbers = [len(matches) for matches in keywords_matches]
        return sum(keywords_numbers)

    @staticmethod
    def calculate_matched_keywords_length(
        text: str,
        keywords: list[str],
    ) -> int:
        """
        计算所有keywords的文本长度。

        这个方法需要和总文本对比时才有意义。

        可以构建中间方法，计算每一个keywords的文本长度。

        Args:
            text (str): 原始文本。
            keywords (list[str]): 需要匹配的多个keywords。

        Returns:
            int: 命中所有keywords的总长度。
        """
        keywords_matches = KeywordsMatcher.match_keywords(
            text=text,
            keywords=keywords,
        )
        count = 0
        for i in range(len(keywords)):
            count += len(keywords[i]) * len(keywords_matches[i])
        return count

    @staticmethod
    def match_keywords(
        text: str,
        keywords: list[str],
    ) -> list[list[str]]:
        """
        一次性对一个原始文本进行多个keyword匹配。

        Args:
            text (str): 原始文本。
            keywords (list[str]): 需要匹配的多个keywords。

        Returns:
            list[list[str]]: 匹配的结果。按照给定的keywords的输入顺序给出结果。
        """
        keywords_matches = []
        for keyword in keywords:
            matches = KeywordsMatcher.match_keyword(
                text=text,
                keyword=keyword,
            )
            keywords_matches.append(matches)
        return keywords_matches

    # ====基础方法。====
    @staticmethod
    def match_keyword(
        text: str,
        keyword: str,
    ) -> list[str]:
        """
        使用正则匹配的方法去查找给定文本中keyword的匹配。

        直接使用keyword作为pattern，而不使用正则语法。

        可以使用python中的原生方法，但精确程度和效率低。

        Args:
            text (str): 原始文本。
            keyword (str): 需要匹配的keyword。

        Returns:
            list[str]: 匹配的结果。实际上是多个完全一样的keyword。
        """
        # 直接使用keyword作为pattern，进行正则匹配。
        pattern = keyword
        matches = re.findall(pattern, text)
        return matches

