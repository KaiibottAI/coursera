#!/usr/bin/env python3

from typing import Counter


file_counts = {"jpg":10,"txt":14,"csv":2,"py":23}
for extension in file_counts:
    print(extension)
#if you use a dictionary in a "for loop", the iteration variable will be the "key" from the dictionary

for ext,amount in file_counts.items(): #use the "items" method that returns a tuple. The First element is the"key", the second value is hte "value"
    print("There are {} files with the .{} extentsion".format(amount,ext))

print(file_counts.keys()) #you can print a special kind of variable for the key
print(file_counts.values()) #you can print a special kind of variable for the value

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal,feature in cool_beasts.items():
    print("{} have {}".format(animal,feature))

#count each time a letter appears in a piece of text
def count_letter(text): #define the function
    result = {} #create an empty dictionary
    for letter in text.lower(): #for loop for each letter in the "text" string variable
        if letter not in result: #if the letter is not in the dictionary "result"
            result[letter] = 0 #add letter to dictionary with "0" value
        result[letter] += 1 #increase the value of the amount of times a letter has been seen in the "text" to the dictionary
    return result #output the result dictionary

print(count_letter("aaaAAaa"))
print(count_letter("How many times do these letters pop up?"))
print(count_letter("Tenant"))