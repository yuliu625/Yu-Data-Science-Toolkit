"""
构建词云进行可视化分析。
"""

from __future__ import annotations

from text_analysis.pre_processing_tools.zh_pre_processing_tools import ZHTextPreProcessingTools

from wordcloud import WordCloud
from pathlib import Path


# if TYPE_CHECKING:


class ZHWordCloudBuilder:
    # ====保留方法。====
    @staticmethod
    def build_wordcloud(
        original_text: str,
        path_to_save: str,
        path_to_stopwords: str | Path,
        wordcloud_kwargs: dict,
        font_path: str | None = 'C:/Windows/Fonts/msyh.ttc',
    ) -> WordCloud:
        # 首先构建stopwords。
        stopwords = ZHWordCloudBuilder.build_stopwords(
            path_to_stopwords=path_to_stopwords,
            custom_stopwords=[' ', '\n', '_'],
        )
        # 对于中文任务，文本处理是必要的。
        processed_text = ZHWordCloudBuilder.build_processed_text(
            original_text=original_text,
            stopwords=stopwords,
        )
        # 制图。
        wordcloud: WordCloud = WordCloud(**{
            **dict(
                width=800, height=400,
                background_color='white',
                font_path=font_path,
                collocations=False,
            ),
            **wordcloud_kwargs,
        }).generate(processed_text)
        wordcloud.to_file(path_to_save)
        return wordcloud

    @staticmethod
    def build_stopwords(
        path_to_stopwords: str,
        custom_stopwords: list[str],
    ) -> set[str]:
        """
        构建stopwords，并根据具体任务需要添加自定义的stopwords。

        Args:
            path_to_stopwords:
            custom_stopwords:

        Returns:
            set[str]:
        """
        stopwords = ZHTextPreProcessingTools.load_stopwords(
            path_to_stopwords=path_to_stopwords,
            custom_stopwords=custom_stopwords,
        )
        return stopwords

    @staticmethod
    def build_processed_text(
        original_text: str,
        stopwords: set[str],
    ) -> str:
        filtered_words = ZHTextPreProcessingTools.tokenize_text_by_jieba(
            text=original_text,
            stopwords=stopwords,
        )
        processed_text = ' '.join(filtered_words)
        return processed_text

