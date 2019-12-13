from spellchecker import SpellChecker
"""
	 INSTEAD OF LOADING IT HERE WE CAN LOAD PARTICULAR JSON BASED ON USER CHOICE
data1 =json.load(open("webster.json")) # read mode is default so need not mention it.
data2 =json.load(open("data.json"))

"""
spell=SpellChecker()
x="IroNN"
y=spell.correction(x)
print(y)