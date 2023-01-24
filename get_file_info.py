import os
from pathlib import Path


for path in Path('.').iterdir():
    info = path.stat()
    # print("+", path.anchor, path.drive, path.name, path.parts, path.root, path.stem, path.suffix, path.suffixes, info.st_blksize, info.st_blocks, info.st_size, info.st_mtime)
    print("+", path.name, info.st_size, info.st_mtime)
    print(os.path.basename(path))
    print(os.path.getsize(path))
    print(os.path.getmtime(path))
    print(os.path.getctime(path))
    print(os.stat(path))
