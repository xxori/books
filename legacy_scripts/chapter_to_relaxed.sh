#!/bin/bash
for i in {4..30}
do
  sed -i "" -r "s/\\\\chapter\{([^}]*)\}/\\\\vspace{1cm}\n\\\\begingroup\n\\\\\let\\\\clearpage\\\\relax\n\\\\chapter{\1}\n\\\\endgroup\n\\\\vspace{-1cm}/g" chapter$i.tex
done
