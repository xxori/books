#!/bin/bash

sed -i "" -r "s|\"([^\"]*)\"|\`\`\1''|g" source.txt
