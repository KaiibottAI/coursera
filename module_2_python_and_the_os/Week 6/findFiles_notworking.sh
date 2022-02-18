#!/bin/bash

>oldfiles.txt

grep ' jane ' ~/data/list.txt | cut -d ' ' -f 3 > ./oldfiles.txt
files=$(grep "jane" ./oldfiles.txt)
for file in $files; do
        echo $file
        if test -e ~/$file; then
                echo "$file" > ./oldfiles.txt
        else
                echo "~/$file does not exist"
        fi
done