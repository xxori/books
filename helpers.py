import re
import os
from config import *


class FileHolder:
    def __init__(self, filename: str):
        self.filename = filename

    def fix_footnotes(self):
        with open(self.filename, "r+") as f:
            text = f.read()
            text = re.sub(r"P\. [\d]+\.\s*", "", text)
            for line in text.split("\n"):
                if tup := re.search(r"^\s*\[(\d+)]\s+(.*)", line):
                    tag, note = tup.group(1, 2)
                    text = text.replace(line + "\n", "")
                    text = re.sub(
                        rf"\[{tag}\]", r"\\footnote{" + note.strip() + "}", text
                    )
            text = re.sub(r"\n*\s*FOOTNOTES:\s*\n*", "", text)
            write_rp(f, text)
        return self

    def _file_sub(self, find, repl):
        with open(self.filename, "r+") as f:
            text = f.read()
            text = re.sub(find, repl, text)
            write_rp(f, text)
        return self

    def fix_underscore_italics(self):
        self._file_sub(r"_([^_]+)_", r"\\textit{\1}")
        return self

    def fix_quotations(self):
        self._file_sub(r'"([^"]+)"', r"``\1''")
        return self


def write_rp(f, text):
    f.truncate(0)
    f.seek(0)
    f.write(text)


def auto_lettrine():
    for i in range(CHAPTERS + 1):
        if os.path.exists(f"chapter{i}.tex"):
            with open(f"chapter{i}.tex", "r+") as f:
                text = f.read()
                text = re.sub(
                    r"(\\chapter\{[^}]*\})\n[\s]*([`']*[A-Za-z])([a-zA-Z`'\"]*)",
                    r"\1\n\\lettrine[lraise=0.1,nindent=0em,slope=-.5em]{\2}{\3}",
                    text,
                )
                write_rp(f, text)


def init_chapters():
    for i in range(CHAPTERS + 1):
        if not os.path.exists(f"chapter{i}.tex"):
            with open(f"chapter{i}.tex", "w+") as f:
                f.write(r"\chapter{}")


if __name__ == "__main__":
    if WORKINGDIR:
        os.chdir(os.path.join(os.getcwd(),WORKINGDIR))
    init_chapters()
    f = FileHolder("source.txt")
