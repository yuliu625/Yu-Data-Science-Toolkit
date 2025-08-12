"""
文本预处理工具。
"""

from __future__ import annotations

import re
import jieba
from pathlib import Path

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:


class ZHTextPreProcessingTools:
    """
    中文文本的预处理方法。
    """
    @staticmethod
    def tokenize_text(
        text: str,
        path_to_stopwords: str | Path | None,
        custom_stopwords: list[str] | set[str],
        tokenize_method: Literal['jieba'],
    ) -> list[str]:
        # 加载stopwords。
        if path_to_stopwords is None:
            stopwords = set(custom_stopwords)
        else:
            stopwords = ZHTextPreProcessingTools.load_stopwords(
                path_to_stopwords,
                custom_stopwords,
            )
        # 进行分词。
        if tokenize_method == 'jieba':
            result = ZHTextPreProcessingTools.tokenize_text_by_jieba(
                text=text,
                stopwords=stopwords,
            )
            return result

    @staticmethod
    def tokenize_text_by_jieba(
        text: str,
        stopwords: list[str] | set[str],
    ) -> list[str]:
        """
        中文任务额外要处理的很麻烦的对于文本进行分词处理。

        Args:
            text (str):
            stopwords (Union[list[str], set[str]]):

        Returns:
            list[str]: 做了分词的结果。
                可使用:
                ```python
                ' '.join(result)
                ```
                获得拼接后的结果。
        """
        words = jieba.cut(text)
        filtered_words = [word for word in words if word not in stopwords]
        return filtered_words

    @staticmethod
    def load_stopwords(
        path_to_stopwords: str | Path,
        custom_stopwords: list[str] | set[str],
    ) -> set[str]:
        """
        从本地路径读取基础的stopwords。

        Args:
            path_to_stopwords (Union[str, Path]):
            custom_stopwords (Union[list[str], set[str]]):

        Returns:
            set[str]: 以set形式返回当前的stopwords，可根据任务需要再进行添加。
        """
        stopwords = set()
        if path_to_stopwords:
            with open(path_to_stopwords, 'r', encoding='utf-8') as f:
                for line in f:
                    stopwords.add(line.strip())
        if custom_stopwords:
            for word in custom_stopwords:
                stopwords.add(word)
        return stopwords

    @staticmethod
    def delete_numbers_and_punctuation(
        text: str,
    ) -> str:
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        return text

    @staticmethod
    def delete_empty_string_in_texts(
        texts: list[str],
    ) -> list[str]:
        return [text for text in texts if text.strip()]

