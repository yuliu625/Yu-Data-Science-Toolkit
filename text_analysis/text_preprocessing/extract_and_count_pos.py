"""
提取词性并进行统计。
"""

from __future__ import annotations

import spacy
from collections import Counter

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def get_pos_result(
    text: str,
    poss: list[str],
    keywords_number: int,
):
    # nlp = spacy.load('en_core_web_sm')
    nlp = spacy.load('en_core_web_lg')
    nlp.max_length = 1000000 * 200  # 使用200G内存
    doc = nlp(text)
    for pos in poss:
        result = extract_and_count_pos(
            doc=doc,
            pos=[pos],
            keywords_number=keywords_number,
        )
        print(result)


def extract_and_count_pos(
    doc: spacy.tokens.doc.Doc,
    pos: list[str],
    keywords_number: int,
):
    """
    提取文本中的某种词性的词，并对它们的还原形式进行计数。
    """
    target_lemmas = []

    for token in doc:
        if token.pos_ in pos:
            target_lemmas.append(token.lemma_)

    lemma_counts = Counter(target_lemmas)
    return lemma_counts.most_common(n=keywords_number)

