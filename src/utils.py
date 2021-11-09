import pathlib
from typing import Union


def load_code(filename: Union[str, pathlib.Path]) -> str:
    with open(filename, "r") as f:
        lines = f.read()
    return lines


def write_code(filename: Union[str, pathlib.Path], text: str):
    with open(filename, "w") as f:
        f.write(text)
