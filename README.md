# FASTA parser exercises

Genome sequences are usually stored in so-called [FASTA files](https://en.wikipedia.org/wiki/FASTA_format), and we will use the same in this class. However, we will not need to full specification of this file format, since genomic data is commonly stored in files that do not use the full set of features.

The subset of of the FASTA format that we will support, we can call it *Simple-FASTA*, can handle all the genomic data set that I have ever seen, but not the data that some protein data bases will export. We don't need those, however, and there is no need to support it for this class. (You can always implement the full specification some later day, if you feel like it).

Still, we need to handle the Simple-FASTA file format, because we need *some* file format for our input genomes, and we might as well choose one that is likely to work with any real-world data we are likely to encounter.

Therefore, you need to write a parser for Simple-FASTA.

In the projects, you will always get your genomic input in Simple-FASTA files. The exercises below should assist you in writing such a parser and test that it works as intended.

## The Simple-FASTA format

A Simple-FASTA file is a plain text file that consists of one or more records, where each record starts with a `>` as the first character on a line. The first line in a record, the line that starts with `>` is the *header* and the remaining lines contain the sequence.

In a regular FASTA file, the header can contain various meta-information about a sequence, but in Simple-FASTA, it will just be the name of the sequence. You get this name by removing the `>` character and any leading or trailing white-space. So, if the header is `> foo `, then the name is just `foo`, not `> foo `, and not `>foo`. Just `foo`. If the header is `> foo bar`, the name is `foo bar`, because we only skip leading and trailing spaces, not spaces in the middle of the string.

The sequence is all the lines that follow the header, until we either see a new header, recognisable by a `>` at the beginning of a line, or the end of the file. Newlines are not considered part of the sequence, so you should remove those and concatenate the lines.

For example, if we have the header

```
> foo
acgtacgt
acgtacgt
```

the the name of the sequence is `foo` and the sequence is `acgtacgtacgtacgt`.

If the Simple-FASTA file looks like this:

```
> foo
acgt
acgt
>bar
tgcatg
ca
```

then there are two records, the first has the name `foo` and sequence `acgtacgt` and the second has the name `bar` and the sequence `tgcatgca`.

## Exercise: Listing records

Write a program, `fasta-recs`, that takes a Simple-FASTA file as input and outputs to `stdout` one record per line, with the header followed by a tab and then the sequence, i.e, the Simple-FASTA file

```
> foo
acgt
acgt
>bar
tgcatg
ca
```

should be output as

```
foo acgtacgt
bar tgcatgca
```

where the space between the sequence name and the sequence is a single tab.

You can test your program by running the `test-fasta-recs.sh` script in the root directory of the repository. It will compare the output of your `fasta-recs` program against the expected output.

In the root of this repository is a script, `fasta-recs` that will run Python on the file `src/fasta-recs.py`, so if you start writing your program from this file, you are good to go.


## Exercise: Extracting subsequences

Once we start searching in genomic sequences, it can be helpful to have a tool that extracts a subsequence from a Simple-FASTA file. With such a tool, or code to a similar effect, we can get the genomic sequence at a given position and check that it matches the pattern we searched for.

As a warmup exercise for that, you should write a tool, `get-subseqs`, that takes one or two files as input. The first should be a Simple-FASTA file and the second should be a file containing coordinates for sub-sequences as described below. If the second file isn't provided on the command-line, or if it is provided as `-`, you should use `stdin`.

The coordinates file consists of zero or more lines of coordinates, where coordinates consist of three tab-separated values: First the sequence name (the name of the Simple-FASTA record), then the start coordinate, and finally the end-coordinate. The coordinates are 1-indexed, so if you program in a language that uses 0-indexing, you need to subtract one from these. You can assume `start <= end`.

The output, written to `stdout`, should be one sub-sequence per line. A sub-sequence goes from the start coordinate to, but not including, the end-coordinate.

If the Simple-FASTA file is

```
> foo
acgtacgt
>bar
tgcatgca
```

and the coordinates are

```
foo 1 5
bar 3 6
```

the output should be

```
acgt
cat
```

You can use the script `test-get-subseqs.sh` to test your program.

In the root of this repository is a script, `get-subsets` that will run Python on the file `src/get-subseqs.py`, so if you start writing your program from this file, you are good to go.
