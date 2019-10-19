def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort(reverse=True)
	solution = [0,float('inf')]
	min = float('inf')
	for num in arrayOne:
		for num2 in arrayTwo:
			if abs(num - num2) < min:
				min = abs(num - num2)
				solution[0] = num
				solution[1] = num2
	return solution