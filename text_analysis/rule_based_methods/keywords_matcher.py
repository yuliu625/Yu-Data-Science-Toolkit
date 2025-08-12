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
        ...

    @staticmethod
    def match_keywords(
        text: str,
        keywords: list[str],
    ) -> list[str]:
        ...

    @staticmethod
    def match_keyword(
        text: str,
        keyword: str,
    ) -> list[str]:
        ...

