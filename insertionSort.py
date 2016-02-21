def insertionSort(l):
	for index in range(1, len(l)):
		valueToSort = l[index]
		position = index

		while position > 0 and valueToSort < l[position - 1]:
			l[position] = l[position - 1]
			position -= 1

		l[position] = valueToSort

	return l