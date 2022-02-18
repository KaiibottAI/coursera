#!/usr/bin/env python3

import re
import sys
import os

file = "/var/log/syslog"

pattern = "INFO"

with open(file) as f:
	print(re.search(r"$pattern", f))