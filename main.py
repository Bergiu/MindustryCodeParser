#!/bin/python3
from src.preprocessor import preprocess
from src.utils import load_code, write_code
from src.parser import setup as setupp, do_parsing
from src.lexer import setup as setupl, do_lexing

import argparse


def load_args():
    parser = argparse.ArgumentParser(description='Advanced Mindusty Logic Compiler.')
    parser.add_argument('filename', type=str, help='The file that should be compiled.')
    parser.add_argument('-o', dest='outfile', nargs="?", action='store',
                        default=None, help='The output file.', type=str)
    parser.add_argument('--linter', dest='linter', action='store_true',
                        default=False, help='If only the linter should be run.')
    return parser.parse_args()


def setup(filename, lint):
    setupl(filename, lint)
    setupp(filename, lint)


if __name__ == '__main__':
    args = load_args()
    text = load_code(args.filename)
    text = preprocess(text, args.filename)
    setup(args.filename, args.linter)
    # print(do_lexing(text))
    out = do_parsing(text)
    if not args.linter:
        if args.outfile is not None:
            write_code(args.outfile, out)
        else:
            print(out)
