"""
jsonline文件的处理方法。

为了jsonlines库能高效处理数据，最好安装:
```shell
pip install orjson ujson
```
"""

from __future__ import annotations

import jsonlines
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class JsonlineProcessor:
    @staticmethod
    def add_records(
        records: list[dict],
        path_to_jsonl_file: str | Path,
    ) -> None:
        with jsonlines.open(path_to_jsonl_file, "a") as writer:
            writer.write_all(records)

