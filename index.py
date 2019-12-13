# DICTIONARY APPLICATION

""" 
	HERE WE ARE LOADING JSON DATA INTO THE PROGRAM WHICH IS TIME CONSUMING AND A WASTE OF MEMORY.
SO INSTEAD OF LOADING THE JSON FILES(WHICH CAN BE VERY LARGE SOMETIMES) WE CAN STORE THE JSON
INTO DATABASE AND USE QUERIES TO ACCESS ONLY THAT PART OF DATA FROM THE DATABASE. THIS PRACTISE
MAKES OUT PROGRAM FAST AND SMALL.

"""
import json
from spellchecker import SpellChecker
"""
	 INSTEAD OF LOADING IT HERE WE CAN LOAD PARTICULAR JSON BASED ON USER CHOICE
data1 =json.load(open("webster.json")) # read mode is default so need not mention it.
data2 =json.load(open("data.json"))

"""
spell=SpellChecker()
def translate(word,choice):
	if (choice==1):
		return data1[word]
	elif (choice==2):
		return data2[word]	
	else:
		return None
try:
	print("Choose your favourite dictionary.")
	choice=int(input("1.Webster Dictionary. 2.Normal Dictionary :" ))
	while (choice not in range(1,3)):
		print("Please Choose 1 or 2")
		choice=int(input("1.Webster Dictionary. 2.Normal Dictionary :" ))

	x=input("Enter a word: ")
	y=spell.correction(x)
	x=x.lower()
	

	if (x!=y.lower()):
		print("Did you mean: ",y,"?")
		if (choice==2):
			data2 =json.load(open("data.json")) # BY LOADING HERE WE CAN ELIMINATE THE NEED TO LOAD UNNECESSARY JSON
			print("\n",y,":",end="")
			for x in translate(y,choice):
				print(x)
		else:
			data1 =json.load(open("webster.json"))# BY LOADING HERE WE CAN ELIMINATE THE NEED TO LOAD UNNECESSARY JSON
			print("\n",y,":",translate(y,choice))
	else:
		if (choice==2):
			data2 =json.load(open("data.json"))# BY LOADING HERE WE CAN ELIMINATE THE NEED TO LOAD UNNECESSARY JSON
			print("\n",x,":",end="")
			for i in translate(x,choice):
				print(i)
		else:
			data1 =json.load(open("webster.json"))# BY LOADING HERE WE CAN ELIMINATE THE NEED TO LOAD UNNECESSARY JSON
			print("\n",x,":",translate(x,choice))
except KeyError as ke:
	# key error arises because we are converting definite nouns to lowercase which are not present in our json
	if (choice==1):
		print("This word doesnt exist in Webster dictionary. Checking in normal dictionary")
		data2 =json.load(open("data.json")) # toc check in normal dictionary load it first.
		definite=translate(x.title(),2)
		if (definite==None):
			print("This word doesn't exist. Try again!")
		else:
			print("Definite Noun: ",definite)
		ke=None # because exception is handled
	if (choice==2):
		definite=translate(x.title(),2)
		if (definite==None):
			print("This word doesn't exist. Try again!")
		else:
			print("Definite Noun: ",definite)
		ke=None # because exception is handled

	if (ke!=None):
		print("This word doesnt exit in dictionary/s")
except ValueError:
	print("Invalid Operation")
finally:
	print("\nThank you for using my dictionary!")