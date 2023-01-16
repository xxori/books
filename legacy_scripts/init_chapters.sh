#!/bin/bash

for i in {1..$CHAPTERS}
do
  echo \\\\chapter{} > chapter$i.tex
done
