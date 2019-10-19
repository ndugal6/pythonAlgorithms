def kadanesAlgorithm(array):
    currentMax = overallMax = array[0]
    for element in array[1:]:
        currentMax = max(element, currentMax + element)
        overallMax = max(currentMax, overallMax)
    return overallMax
