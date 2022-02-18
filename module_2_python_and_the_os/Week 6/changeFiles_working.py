#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as file:
        for line in file.readlines():
                oldLine = line.strip()
                newLine = line.strip().replace("jane","jdoe")
                #oldDir = "~" + oldLine
                #newDir = "~" + newLine
                #print("~" + oldLine)
                #print("~" + newLine)
                #print(line.strip().replace("jane","jdoe"))
                subprocess.run(["mv",oldLine,newLine])