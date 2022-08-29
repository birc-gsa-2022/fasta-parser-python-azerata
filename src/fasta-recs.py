
from __future__ import annotations
import argparse
from dataclasses import dataclass
import sys
from typing import TextIO




def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    print(dostuff(args.fasta))

    args.fasta.close()

def dostuff(gaffel:TextIO)->SeqLib:
    seqs = SeqLib()
    name = ""
    tmp:list[str] = []
    for line in gaffel:
        if line[0] == '>':
            if name:
                seq = ''.join(tmp)
                seqs.add(Sequence(name, seq))
            name = line[1::].strip()
            tmp:list[str] = []
        else:
            tmp.append(line.strip())
    if name:
        seq = ''.join(tmp)
        seqs.add(Sequence(name, seq))
    return seqs

@dataclass
class Sequence:
    name: str
    seq: str

    def __repr__(self) -> str:
        return f'{self.name}\t{self.seq}'
    
    def __str__(self) -> str:
        return self.__repr__()

class SeqLib(object):
    def __init__(self) -> None:
        self.library:list[Sequence] = []
    
    def __repr__(self) -> str:
        rep = [seq.__str__() for seq in self.library]
        return '\n'.join(rep)
    
    def add(self, seq:Sequence) -> None:
        self.library.append(seq)
        

if __name__ == '__main__':
    main()


