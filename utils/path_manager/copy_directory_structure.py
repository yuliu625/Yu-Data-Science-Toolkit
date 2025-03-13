from pathlib import Path


def copy_directory_structure(source_dir: Path, target_dir: Path):
    """
    复制一个文件夹下的文件树结构。
    仅复制文件夹，不复制文件。
    Args:
        - source_dir: 原始文件夹。
        - target_dir: 目标文件夹。
    """
    # 简单检验，至少目标文件夹初始路径是存在的。
    target_dir.mkdir(parents=True, exist_ok=True)
    # 遍历所有的文件，但仅处理是文件夹的情况。
    for sub_dir in source_dir.rglob('*'):
        if sub_dir.is_dir():
            # 使用相对路径
            relative_path = sub_dir.relative_to(source_dir)
            # 组合，构建新的路径
            target_sub_dir = target_dir / relative_path
            target_sub_dir.mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    pass
