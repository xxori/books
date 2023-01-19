# books
Typesetting with LaTeX with Python.

Can be used for digital reading, or print-on-demand prints with Lulu, Amazon KDP, etc...

---
`How to typeset a new book`

1. Find a public domain book (i.e. before circa 1930)
2. Download a .rtf or .txt file from the internet (use `rtf2latex2e` if a .rtf source is available)
3. Rename `config.py.template` to `config.py` and edit the fields.
4. Use `helpers.py` to tidy up the source code (i.e. correct quotations, collapse newline, fix underline italics, correct footnotes) and fix formatting. Uncomment and/or comment functions to suit your needs.
6. Format the title page as well as the introduction, appendix, etc. Again, use `helpers.py` or do this manually (might be faster?)
7. Profit
