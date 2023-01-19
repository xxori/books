#!/bin/bash

for i in {2..30}
do
  sed -i "" -r "s/(\\\\chapter\{[^}]*\})/\1\n\\\\thispagestyle\{pter\}/g" chapter$i.tex
done
