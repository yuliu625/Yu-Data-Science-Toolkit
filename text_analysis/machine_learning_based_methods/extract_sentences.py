"""
将原始文本拆分为多个句子。
"""

from __future__ import annotations

import spacy
from nltk.tokenize import sent_tokenize

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


# def get_sentences_result(
#     texts: list[str],
# ) -> list[list[str]]:
#     sentences_result = [
#         sent_tokenize(text)
#         for text in texts
#     ]
#     return sentences_result


def get_sentences_result(
    texts: list[str],
) -> list[list[str]]:
    # python -m spacy download en_core_web_lg
    # nlp = spacy.load('en_core_web_sm')
    nlp = spacy.load('en_core_web_lg')
    nlp.max_length = 1000000 * 200  # 使用200G内存
    sentences_result = []
    for text in texts:
        doc = nlp(text)
        sentences = [sent.text for sent in doc.sents]
        sentences_result.append(sentences)
    return sentences_result


def extract_sentences(
    text: str,
) -> list[str]:
    # nlp = spacy.load('en_core_web_sm')
    nlp = spacy.load('en_core_web_lg')
    nlp.max_length = 1000000 * 200  # 使用200G内存
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

