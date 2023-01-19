import re
import shutil
import os
from config import *
import jinja2

env = jinja2.Environment(
    block_start_string = "\\BLOCK{",
    block_end_string = "}",
    variable_start_string = "\\VAR{",
    variable_end_string = "}",
    comment_start_string = "\\#{",
    comment_end_string = "}",
    line_statement_prefix = "%%",
    line_comment_prefix = "%#",
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath(WORKING_DIR)),
)


class FileHolder:
    def __init__(self, filename: str):
        self.filename = filename

    def fix_newlines(self):
        # TODO: Find a better method so Tamil texts aren't formatted weirdly
        self._file_sub(r"\n\n", r"ඞ")  # Heheheha
        self._file_sub(r"\n", r"")
        self._file_sub(r"ඞ", r"\n\n")
        return self

    def fix_latex(self):
        self._file_sub(r"\\vspace\{[^}]*\}\n", "")
        self._file_sub(r"\\baselineskip=.*\n", "")
        self._file_sub(r"\\leftskip=.*\n", "")
        self._file_sub(r"\\parindent=.*\n", "")
        self._file_sub(r'\\texttt\{"\}', '"')
        return self

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

    def fix_underscore_italics(self):
        self._file_sub(r"_([^_]+)_", r"\\textit{\1}")
        return self

    def fix_quotations(self):
        self._file_sub(r'"([^"\n]+)"', r"``\1''")
        return self

    def _file_sub(self, find, repl):
        with open(self.filename, "r+") as f:
            text = f.read()
            text = re.sub(find, repl, text)
            write_rp(f, text)
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
    for i in range(1, CHAPTERS + 1):
        if not os.path.exists(f"chapter{i}.tex"):
            with open(f"chapter{i}.tex", "w+") as f:
                f.write(r"\chapter{}")


def init_root():
    # Run this before chdir to WORKING_DIR
    if not os.path.exists(os.path.join(os.getcwd(), WORKING_DIR, ROOT_FILE)):
        shutil.copy(
            os.path.join(os.getcwd(), "Template", "book.tex"),
            os.path.join(WORKING_DIR, ROOT_FILE),
        )


def write_template():
    template = env.get_template(ROOT_FILE)
  
    with open(ROOT_FILE, "r+") as f:
        if r"\VAR" in f.read():
            ftext = template.render(**CFG_VARS)
            f.truncate(0)
            f.write(ftext)


if __name__ == "__main__":
    # init_root()

    if WORKING_DIR:
        os.chdir(os.path.join(os.getcwd(), WORKING_DIR))
    if SOURCE:
        f = FileHolder(SOURCE)
    else:
        f = FileHolder("soure.txt")
    # write_template()
    # init_chapters()
    f.fix_latex().fix_newlines().fix_quotations()
