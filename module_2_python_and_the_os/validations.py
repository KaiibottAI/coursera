#!/usr/bin/env python3

def validate_user(username, minlen):
	#this forces the username to be a string. If not, an error will raise that we provided.
	assert type(username) == str, "username must be a string"
	if minlen < 1:
		raise ValueError("minlen must be at least 1")
	if len(username) < minlen:
		return False
	if not username.isalnum():
		return False
	return True