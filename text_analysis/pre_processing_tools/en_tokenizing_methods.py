"""
文本预处理工具。

对英文文本进行分词化的方法，用于进行基础文本分析。

扩展:
    - spacy: 该文件的方法基于nltk，主要为学术目的。可使用spacy获得更高效率。
"""

from __future__ import annotations

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ENTokenizingMethods:
    """
    基于nltk的分词方法。

    主要方法:
        - simple_tokenize_text: 简单的的基于re的分词方法。
        - tokenize_text: 基于nltk的标准分词方法。
        - download_for_nltk: 下载该工具类使用nltk的必要依赖。
    """
    # ====暴露方法。====
    @staticmethod
    def simple_tokenize_text(
        text: str,
    ) -> list[str]:
        """
        简单的分词方法。

        基于python的基础工具，可以快速构建分词。

        Args:
            text (str): 原始文本。

        Returns:
            list[str]: 已经处理好的分词列表。
        """
        pattern = r'\b\w+\b'  # 移除标点，按空格分割。
        tokens = re.findall(pattern, text.lower())  # 以小写字母进行处理。
        return tokens

    # ====暴露方法。====
    @staticmethod
    def tokenize_text(
        text: str,
    ) -> list[str]:
        tokens = ENTokenizingMethods.get_tokens(text=text)
        filtered_tokens = ENTokenizingMethods.filter_stopwords(tokens=tokens)
        result_tokens = ENTokenizingMethods.lemmatize_tokens(tokens=filtered_tokens)
        return result_tokens

    # ====工具方法。====
    @staticmethod
    def get_tokens(
        text: str,
    ) -> list[str]:
        """
        使用nltk的word_tokenize进行分词。

        Args:
            text (str): 原始文本。

        Returns:
            list[str]: 已经处理好的分词列表。
        """
        tokens = word_tokenize(
            text=text,
            language='english',
        )
        return tokens

    # ====工具方法。====
    @staticmethod
    def filter_stopwords(
        tokens: list[str],
    ) -> list[str]:
        """
        去除停用词。

        只保留字母，会去除标点符号和数字。

        Args:
            tokens (list[str]): 待处理的分词列表。

        Returns:
            list[str]: 过滤了停用词的分词列表。
        """
        # 使用nltk提供的停用词。
        stop_words = set(stopwords.words('english'))
        # 逐一检查进程过滤。
        filtered_tokens = [
            word for word in tokens if word not in stop_words and word.isalpha()
        ]
        return filtered_tokens

    # ====工具方法。====
    @staticmethod
    def lemmatize_tokens(
        tokens: list[str],
    ) -> list[str]:
        """
        进行词性还原。

        Args:
            tokens (list[str]): 待处理的分词列表。

        Returns:
            list[str]: 已经处理好的分词列表。
        """
        lemmatizer = WordNetLemmatizer()
        # 对每个词进行词性还原。
        lemmas = [lemmatizer.lemmatize(word) for word in tokens]
        return lemmas

    # ====工具方法。====
    @staticmethod
    def download_for_nltk() -> None:
        """
        下载nltk进行分词操作的必要工具。
        """
        nltk.download('punkt')  # from nltk.tokenize import word_tokenize
        nltk.download('stopwords')  # from nltk.corpus import stopwords
        nltk.download('wordnet')  # from nltk.stem import WordNetLemmatizer

