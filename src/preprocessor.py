import re
import pathlib
from typing import List, Union

from src.utils import load_code


def preprocess(text: str, filename: str) -> str:
    text = repair_eof(text)
    return text


def repair_eof(text) -> str:
    if text[len(text) - 1] is not "\n":
        text += "\n"
    return text
