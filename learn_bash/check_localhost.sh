#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
	echo "Everything looks good"
else
	echo "Missing 127.0.0.1 from etc/hosts"
fi