"""
对于高维embeddings降维的方法。
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:


class EmbeddingsDimensionalityReductionMethod:
    @staticmethod
    def reduce_dimension(
        embeddings_list: list[list[list[float]]],
        label_names: list[str],
        model_kwargs: dict,

        reduce_method: Literal['umap', 'tsne', 'pca'],
    ) -> pd.DataFrame:
        if reduce_method == 'umap':
            return EmbeddingsDimensionalityReductionMethod.reduce_dimension_by_umap(
                embeddings_list=embeddings_list,
                label_names=label_names,
                model_kwargs=model_kwargs,
            )
        elif reduce_method == 'tsne':
            return EmbeddingsDimensionalityReductionMethod.reduce_dimension_by_tsne(
                embeddings_list=embeddings_list,
                label_names=label_names,
                model_kwargs=model_kwargs,
            )
        elif reduce_method == 'pca':
            return EmbeddingsDimensionalityReductionMethod.reduce_dimension_by_pca(
                embeddings_list=embeddings_list,
                label_names=label_names,
                model_kwargs=model_kwargs,
            )

    # ====暴露方法。====
    @staticmethod
    def reduce_dimension_by_umap(
        embeddings_list: list[list[list[float]]],
        label_names: list[str],
        model_kwargs: dict,
    ) -> pd.DataFrame:
        all_embeddings, labels = EmbeddingsDimensionalityReductionMethod.get_all_embeddings_and_labels(
            embeddings_list=embeddings_list,
            label_names=label_names,
        )
        reducer = umap.UMAP(**model_kwargs)
        embedding_2d = reducer.fit_transform(all_embeddings)
        df = EmbeddingsDimensionalityReductionMethod.get_df_by_embedding_2d(
            embedding_2d=embedding_2d,
            labels=labels,
        )
        return df

    # ====暴露方法。====
    @staticmethod
    def reduce_dimension_by_tsne(
        embeddings_list: list[list[list[float]]],
        label_names: list[str],
        model_kwargs: dict,
    ) -> pd.DataFrame:
        all_embeddings, labels = EmbeddingsDimensionalityReductionMethod.get_all_embeddings_and_labels(
            embeddings_list=embeddings_list,
            label_names=label_names,
        )
        reducer = TSNE(**model_kwargs)
        embedding_2d = reducer.fit_transform(all_embeddings)
        df = EmbeddingsDimensionalityReductionMethod.get_df_by_embedding_2d(
            embedding_2d=embedding_2d,
            labels=labels,
        )
        return df

    # ====暴露方法。====
    @staticmethod
    def reduce_dimension_by_pca(
        embeddings_list: list[list[list[float]]],
        label_names: list[str],
        model_kwargs: dict,
    ) -> pd.DataFrame:
        all_embeddings, labels = EmbeddingsDimensionalityReductionMethod.get_all_embeddings_and_labels(
            embeddings_list=embeddings_list,
            label_names=label_names,
        )
        reducer = PCA(**model_kwargs)
        embedding_2d = reducer.fit_transform(all_embeddings)
        df = EmbeddingsDimensionalityReductionMethod.get_df_by_embedding_2d(
            embedding_2d=embedding_2d,
            labels=labels,
        )
        return df

    # ====工具方法。====
    @staticmethod
    def get_df_by_embedding_2d(
        embedding_2d: np.ndarray,
        labels: np.ndarray,
    ) -> pd.DataFrame:
        df = pd.DataFrame({
            'x': embedding_2d[:, 0],
            'y': embedding_2d[:, 1],
            'group': labels,
        })
        return df

    # ====工具方法。====
    @staticmethod
    def get_all_embeddings_and_labels(
        embeddings_list: list[list[list[float]]],
        label_names: list[str],
    ) -> tuple[np.ndarray, np.ndarray]:
        groups_embeddings = [
            np.array(embeddings)
            for embeddings in embeddings_list
        ]
        all_embeddings = np.vstack(groups_embeddings)
        labels = []
        for i in range(len(label_names)):
            # a = [label_names[i]] * len(embeddings_list[i])
            labels.extend([label_names[i]] * len(embeddings_list[i]))
        labels = np.array(labels)
        return all_embeddings, labels

