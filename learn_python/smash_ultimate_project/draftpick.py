#!/usr/bin/env python3

#import dependent modules
import os
import csv
import random
import pandas as pd

#from DraftOrder import DraftList

#list all the important docs ahead of time
teams_csv = "csv_files\Smash Team.csv"
draftOrder = "csv_files\DraftOrder.txt"
smashCharacters = "csv_files\Smash Ultimate Characters - Smash Characters.csv"
CharacterList = []

with open(smashCharacters, "r") as smashCharactersFile: #open the Smash Characters csv
    smashCharacters_reader = csv.DictReader(smashCharactersFile) #read the csv as a Dicitonary
    for row in smashCharacters_reader: #for each row in the dictionary
        if row["Unlocked Characters"] == "": #if the "Unlocked Characters" key is empy (since there are a few empty values in the csv), skip the line
            continue
        #print("Still available characters {}".format(row["Unlocked Characters"])) #print if the characters is still available in the list
        CharacterList.append(row["Unlocked Characters"]) #add the available characters to a list for index ease
    for index,characterName in enumerate(CharacterList): #create the index from the list
        print("{} - {}".format(index + 1, characterName)) #print the index + character name for 1) Counting how much is left and 2) Easier to type in "2" than character name

#CharacterList[index]
#print(CharacterList[int(input("Enter the number of the Character: "))-1]) #ask the person for input of the index of Character Names available
UserNum = ""
while len(CharacterList) > 0: #while the character list still has names to choose from
    UserNum = int(input("Enter the number of the Character: \n(Must be a number)")) #ask the user for the number of the character they want
    UserChoice = CharacterList[UserNum-1] #print the character they selected
    CharacterList.remove(CharacterList[UserNum-1]) #remove the character they selected from the list of available characters
    
    for index,characterName in enumerate(CharacterList): 
        print("{} - {}".format(index+1,characterName)) #show the list of available characters
    print("You have picked {}!".format(UserChoice))
    print("There are {} left to choose from".format(len(CharacterList))) #let the user know how many are left to choose from
    if len(CharacterList) == 0:
        print("The characters have all be picked!")
