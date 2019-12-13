"""
THIS IS AN ALTERNATE WAY AND INFACT AND EFFECTIVE WAY TO IMPLEMENT THIS APPLICATION
BECAUSE IM NOT USING TWO DICTIONARIES AND NOT USING EXECPTION HANDLING WHICH MADE 
THIS CODE SIMPLE. I USED DEFAULT ARGUMENT LOGIC WHICH MADE THIS MORE LOGICAL.
"""
import json
from spellchecker import SpellChecker
spell=SpellChecker()
data=json.load(open("data.json"))

def translate(word,misc=0):
	if word in data: # checking general words
		return data[word]
	elif word.title() in data: # checking definite nouns 
		return "Definite noun:{}:{}".format(word.title(),data[word.title()])
	elif word.upper() in data: #  checking acronyms
		return "Acronym:{}:{}".format(word.upper(),data[word.upper()])
	elif spell.correction(word) in data: # in case of spelling mistakes
		if (misc==0):	
				correct=spell.correction(word)
				return "Did you mean '{}'? \n \t {}".format(correct,translate(correct,1))
	else:
		return "Word Not found. Please check again"
print("welome to my dictionary.")
word=input("Enter the word: ")
word=word.lower()
print(translate(word,0))
print("Thank you for using my dictionary")


