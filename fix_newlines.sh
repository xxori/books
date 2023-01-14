#!/bin/bash

sed -i "" "s/\n\n/å/g" source.tex
sed -i "" "s/\n//g" source.tex
sed -i "" "s/å/\r\r/g" source.tex
