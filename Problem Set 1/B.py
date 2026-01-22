import sys
import pathlib
import io


if not sys.stdin.isatty():
    data = sys.stdin.read()
else:
    data = io.StringIO(pathlib.Path("Problem Set 1/B.txt").read_text())

