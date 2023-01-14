#!/bin/bash

sed -i "" -r "s|\_([^\_]*)\_|\\\\textit{\1}|g" source.txt
