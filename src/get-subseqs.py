import argparse
import sys
from typing import TextIO


def make_library(f: TextIO) -> dict[str, str]:
    out: dict[str, str] = {}
    name = ""
    tmp: list[str] = []
    for line in f:
        if line and line[0] == '>':
            if name:
                out[name] = ''.join(tmp)
            name = line[1::].strip()
            tmp: list[str] = []
        else:
            tmp.append(line.strip())
    if name:
        out[name] = ''.join(tmp)
    return out


def get_sub(library: dict[str, str], f: TextIO) -> list[str]:
    out: list[str] = []
    coord_lib: list[tuple[str, int, int]] = []
    tmp = f.readlines()
    for line in tmp:
        if line:
            coord = line.split()
            coord_lib.append((coord[0], int(coord[1]), int(coord[2])))

    for coord in coord_lib:
        out.append(library[coord[0]][coord[1]-1:coord[2]-1])
    return out


def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()

    library = make_library(args.fasta)
    out = get_sub(library, args.coords)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
