#!/bin/bash

sed -i "" -r "s/\n\n/ç/g" source.txt
sed -i "" -r "s/\n//g" source.txt
sed -i "" -r "s/ç/\r\r/g" source.txt
