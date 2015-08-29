def is_unique(string):
	"""Checks that all characters in a string are unique. Returns true/false."""

	unique = {}
	for character in string:
		if unique.get(character):
			return false
		unique[character] = 1
	return True

def check_permutation(string1, string2):
	"""Given two strings, check to see if one is a permutation of the other."""

	dict1 = {}
	dict2 = {}

	# Count how many of each letter is in both strings
	for letter in string1:
		dict1[letter] = dict1.setdefault(letter, 0) + 1

	for letter in string2:
        dict2[letter] = dict2.setdefault(letter, 0) + 1

    # Dictionaries are inherently unordered, so two dictionaries are
    # equal to one another iff they contain the same data, regardless of order
    return dict1 == dict2

def urlify(string):
	"""Replace all the spaces in a string with '%20'."""

	result = ""
	for character in string:
		if character == " ":
			result += "%20"
		else:
			result += character
	return result

