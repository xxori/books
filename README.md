# books
Typesetting with LaTeX and a bunch of automation tools (bash,perl,vim,sed,...)

Can be used for digital reading, or print-on-demand prints with Lulu, Amazon KDP, etc..

---
`How to typeset a new book`

1. Find an public domain book (i.e. before 1930 or whereabouts)
2. Download an rtf or txt file from the internet (use rtf2latex2e if an rtf source is available)
3. Use `init_chapters.sh` and manually copy chapter titles
4. Use scripts in this repo to tidy up the source (some require perl, nvim, sed, etc. to be installed) i.e. correct quotations, collapse newline, fix underline italics, correct footnotes
5. Copy each chapter's text using e.g. vim visual mode (You may need to intervene manually in some cases i.e. some tex files produces by rtf2latex2e contain \texttt{"} or {\LARGE{} }
6. Format title page as well as introduction, appendix, etc
7. Profit
