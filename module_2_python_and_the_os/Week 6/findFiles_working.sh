#!/bin/bash

> oldFiles.txt

files=$(grep " jane " ~/data/list.txt | cut -d' ' -f3)
for file in $files; do
        echo $file
        if test -e ~/$file; then
                echo "$file" >> ./oldFiles.txt
        else
                echo "$file does not exist"
        fi
done
