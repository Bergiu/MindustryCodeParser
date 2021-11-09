#!/bin/python3

from src.utils import load_code
from src.parser import do_linting, set_filename as sfp
from src.lexer import set_filename as sfl

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    text = load_code(filename)
    sfl(filename)
    sfp(filename)
    do_linting(text)
