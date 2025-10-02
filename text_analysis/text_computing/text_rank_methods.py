"""
基于text-rank的分析方法。
"""

from __future__ import annotations

import spacy
import pytextrank

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def get_text_rank_result(
    text: str,
    text_rank_config: dict,
    keywords_number: int,
):
    nlp = spacy.load('en_core_web_sm')
    # nlp = spacy.load('en_core_web_lg')
    nlp.add_pipe(
        'textrank',
        config=text_rank_config,
    )
    nlp.max_length = 1000000 * 200  # 使用200G内存
    doc = nlp(text)
    for phrase in doc._.phrases[:keywords_number]:
        # phrase.text
        # phrase.rank
        # phrase.count
        # phrase.chunks
        print(f"Text: {phrase.text}. \t Rank: {phrase.rank}. \t Count: {phrase.count}.")

