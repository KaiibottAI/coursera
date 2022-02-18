#!/usr/bin/env python3

import psutil

def check_disk_usage(disk,min_absolute,min_percent):
	du = shutil.dick_usage(disk)
	#calculate the percentage of diskspace
	percent_free = 100 * du.free / du.total
	#calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_absolute:
		return False
	return True

# Check for at least 2 GB and 10% free
if not check_disk_usage("/", 2*2*30,10):
	print("ERROR: Not enough disk space")
	return 1

print("Everhting is okay")
return 0