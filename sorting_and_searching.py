def sorted_merge(list1, list2):
	"""Given two sorted arrays, merge them together in sorted order."""

	result = []

	# Run until both lists have been emptied into the results list
	while len(list1) > 0 or len(list2) > 0:
		if list1 == []:
			result.append(list2.pop(0))
		elif list2 == []:
			result.append(list1.pop(0))
		elif list1[0] < list2[0]:
			result.append(list1.pop(0))
		else:
			result.append(list2.pop(0))

	return result

def group_anagrams(array):
    """Given a list of strings, sort the list such that any anagrams appear next to one another."""

    result = {}

    for string in array:
        listed = list(string)
        listed.sort()
        key = ''.join(listed)
        if result.get(key):
            result[key].append(string)
        else:
            result[key] = [string]

    print result.values()