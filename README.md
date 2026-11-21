# brave1

`main.py` (Python 3.13, standard library only) writes one fixed UTF-8 text, with no trailing newline, to `/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set. It exits non-zero if the text is not 1 to 280 code points or is only white space. Run it with `python3 main.py` or `MAKEFUN_OUTPUT_DIR=out/a python3 main.py`. The text, 226 code points:

```
No one is waiting on the far side of this sentence.
The next word can come slowly.
It does not have to be right yet. Only next.

A rower cannot see the shore.
She faces where she has been,
and pulls,
and the boat goes forward.
```
