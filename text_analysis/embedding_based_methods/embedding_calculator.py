"""
使用embedding的基础计算方法。

为了方便性:
    - 目前的实现方法是基于langchain的embedding-model。
        - 部署很容易。
        - 可以具体定制方法。

可以进行的改进:
    - HuggingfaceEmbeddings: 支持的模型更多，并且可以直接计算相似度。
    - vector-store: langchain中提供了vector-store，可以高效计算和查询。
"""

from __future__ import annotations

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.embeddings import Embeddings


class LangchainEmbeddingCalculator:
    # ====暴露方法。====
    @staticmethod
    def batch_equal_calculate_multi_query_weighted_scores(
        query_embeddings: list[list[float]],
        text_embeddings: list[list[float]],
    ) -> list[float]:
        # 给予所有query相等的权重。
        query_weight = [1 for _ in query_embeddings]
        return LangchainEmbeddingCalculator.batch_calculate_multi_query_weighted_scores(
            query_embeddings=query_embeddings,
            text_embeddings=text_embeddings,
            query_weights=query_weight,
        )

    # ====暴露方法。====
    @staticmethod
    def batch_calculate_multi_query_weighted_scores(
        query_embeddings: list[list[float]],
        text_embeddings: list[list[float]],
        query_weights: list[float],
    ) -> list[float]:
        """
        给予多个query，根据权重求和各个文本对于一组查询的相似度。

        为了更好的可解释性，可传入仅一个query。

        Args:
            query_embeddings: (list[list[float]]): 一组query的embedding。
            text_embeddings: (list[list[float]]): 一组文本的embedding。
            query_weights: (list[float]): 各query按照输入顺序的权重。

        Returns:
            list[float]: 每个文本对于一组query的相似度。
        """
        query_weights = np.array(query_weights)
        # 归一化。
        query_weights = query_weights / np.sum(query_weights)
        # 批量计算原始权重。
        similarity_matrix = LangchainEmbeddingCalculator.calculate_cosine_similarities(
            query_embeddings=query_embeddings,
            text_embeddings=text_embeddings,
        )
        weight_matrix = similarity_matrix * query_weights[:, np.newaxis]
        weight_average_similarity_by_col = np.sum(weight_matrix, axis=0)
        return weight_average_similarity_by_col.tolist()

    # ====工具方法。仅封装cosine_similarity方法。====
    @staticmethod
    def calculate_cosine_similarities(
        query_embeddings: list[list[float]],
        text_embeddings: list[list[float]],
    ) -> np.ndarray:
        """
        cosine_similarity的计算方法。

        基于sklearn中提供的方法，使用np.ndarray实现加速。

        Args:
            query_embeddings: (list[list[float]]): 一组query的embedding。
            text_embeddings: (list[list[float]]): 一组文本的embedding。

        Returns:
            np.ndarray: 相似度矩阵。
        """
        similarity = cosine_similarity(
            query_embeddings,
            text_embeddings,
        )
        return similarity

    # ====工具方法。仅封装langchain_core.Embeddings方法。====
    @staticmethod
    def calculate_embeddings(
        embedding_model: Embeddings,
        texts: list[str],
    ) -> list[list[float]]:
        """
        将一组文本编码为embeddings。

        这里使用的是langchain中提供的embedding_model。

        Args:
            embedding_model (Embeddings): langchain中符合Embeddings定义的实例。
            texts (list[str]): 一组文本。

        Returns:
            list[list[float]]: 编码后的embeddings。
        """
        embeddings = embedding_model.embed_documents(
            texts=texts,
        )
        return embeddings

