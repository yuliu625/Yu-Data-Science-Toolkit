"""
文件数量检查器。
"""

from pathlib import Path


def check_file_number(dir_path: str | Path) -> int:
    """
    检测一个文件夹下有多少个文件。

    Args:
        dir_path: 需要检测的文件夹路径。可以是字符串或Path对象。
    Return:
        不区分文件或文件夹类型的数量结果。
    """
    dir_path = Path(dir_path)
    print(len(list(dir_path.iterdir())))
    return len(list(dir_path.iterdir()))


if __name__ == '__main__':
    check_file_number(r"D:\document\code\deep_learning\paper\news_agent\dataset_pipeline\original\utils")
