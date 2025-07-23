"""
对于jsonline文件的专门加速方法。
"""

from __future__ import annotations

import math
import jsonlines
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class JsonlineAccelerator:
    @staticmethod
    def split_jsonl_file(
        input_file_path: str | Path,
        output_dir: str | Path,
        num_files: int,
    ) -> None:
        # 处理路径。
        input_file_path = Path(input_file_path)
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)
        # 读取原始文件。
        with jsonlines.open(input_file_path, 'r') as reader:
            # for obj in reader:
            #     lines.append(obj)
            data = list(reader)
        # 决定每个chunk大小的计算方法。
        chunk_size = math.ceil(len(data) / num_files)
        # 做多个切片，不断写入文件。
        for i in range(num_files):
            chunk = data[i * chunk_size:(i + 1) * chunk_size]
            if not chunk:
                continue
            # 约定命名方式简单为数字编号。
            output_path = output_dir / f'{i}.jsonl'
            with jsonlines.open(output_path, 'w') as writer:
                writer.write_all(chunk)
            print(f"Saved {i} in {output_path}")

    @staticmethod
    def concat_jsonl_files(
        input_dir: str | Path,
        output_file_path: str | Path,
    ) -> None:
        # 处理路径。
        input_dir = Path(input_dir)
        output_file_path = Path(output_file_path)
        # 读取每一个jsonl文件。
        data = []
        for input_file_path in input_dir.iterdir():
            if input_file_path.is_file() and input_file_path.suffix == '.jsonl':
                with jsonlines.open(input_file_path, 'r') as reader:
                    data.append(list(reader))
        # 将结果写入目标文件。
        with jsonlines.open(output_file_path, 'w') as writer:
            writer.write_all(data)

    @staticmethod
    def split_big_jsonl_file(
        input_file_path: str | Path,
        output_dir: str | Path,
        num_files: int,
    ) -> None:
        input_file_path = Path(input_file_path)
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)

    @staticmethod
    def concat_big_jsonl_files(
        input_dir: str | Path,
        output_file_path: str | Path,
    ) -> None:
        ...

