#!/bin/bash

sed -i "" -r "s/\n\n\([a-z]\)\C/ \1/g" source.tex
