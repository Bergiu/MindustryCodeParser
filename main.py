#!/bin/python3
from src.preprocessor import preprocess
from src.utils import load_code, write_code
from src.parser import setup as setupp, do_parsing
from src.lexer import setup as setupl, do_lexing

import argparse


def load_args():
    parser = argparse.ArgumentParser(description='Mindusty Logic Parser.')
    parser.add_argument('filename', type=str, help='The file that should be parsed.')
    return parser.parse_args()


def setup(filename):
    setupl(filename)
    setupp(filename)


if __name__ == '__main__':
    args = load_args()
    text = load_code(args.filename)
    text = preprocess(text, args.filename)
    setup(args.filename)
    # print(do_lexing(text))
    do_parsing(text)
