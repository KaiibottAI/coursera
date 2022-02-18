#!/usr/bin/env python3

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothing,colors in wardrobe.items(): #clothing = wardrobe.keys(), colors = wardrobe.values() but the value is a list
	for color in colors: #color in colors is going over each value in the colors list
		print("{} {}".format(color,clothing))