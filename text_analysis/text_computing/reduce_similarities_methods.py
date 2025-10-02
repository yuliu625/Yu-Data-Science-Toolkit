"""
降低维度的方法。
"""

from __future__ import annotations

# import statistics

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ReduceSimilaritiesMethods:
    """
    多个similarities降低为一个similarity的方法。
    """
    @staticmethod
    def calculate_mean_similarity(
        similarities: list[float],
    ) -> float:
        return sum(similarities) / len(similarities)

    @staticmethod
    def calculate_max_similarity(
        similarities: list[float],
    ) -> float:
        return max(similarities)

