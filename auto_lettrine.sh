#!/bin/bash
for i in $(seq $CHAPTERS) 
do
  nvim -c "$(cat nvim_replace.nvim)" -c wq chapter$i.tex
done
