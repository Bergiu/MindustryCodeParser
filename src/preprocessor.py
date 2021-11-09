import re
import pathlib
from typing import List, Union

from src.utils import load_code


def preprocess(text: str, filename: str) -> str:
    text = "\n".join(_preprocess_intern(text, filename))
    text = repair_eof(text)
    return text


def _preprocess_intern(text: str, filename: Union[str, pathlib.Path]) -> List[str]:
    return replace_includes(text, filename)


def repair_eof(text) -> str:
    if text[len(text) - 1] is not "\n":
        text += "\n"
    return text


def replace_includes(text: str, filename: Union[str, pathlib.Path]) -> List[str]:
    lines = text.split("\n")
    new_lines = []
    for index, line in enumerate(lines):
        line = line.strip()
        res = re.match("^import ([a-zA-Z/_.]+)[ ]?", line)
        if res is not None:
            new_filename = res.group(1)
            relative_file = pathlib.Path(filename).parent.joinpath(new_filename)
            imported_code = load_code(relative_file)
            processed_code = _preprocess_intern(imported_code, relative_file)
            new_lines.extend(processed_code)
        else:
            new_lines.append(line)
    return new_lines