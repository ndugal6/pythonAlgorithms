def bubbleSort(array):
	hasNeedToSort = True
	while(hasNeedToSort):
		hasNeedToSort = False
		for index in range(len(array)-1):
			if array[index] > array[index+1]:
				hasNeedToSort = True
				array[index], array[index+1] = array[index+1], array[index]
	return array