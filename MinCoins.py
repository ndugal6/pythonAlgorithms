def minNumberOfCoinsForChange(n, denoms):
    if n == 0:
        return 0
    denoms.sort(reverse=True)
    largest = denoms[0]
    if n % largest == 0:
        return n / largest
    if len(denoms) == 1:
        return -1
    if largest > n:
        return minNumberOfCoinsForChange(n, denoms[1:])

    coinsAdded = int(n / largest)
    additionalNeeded = minNumberOfCoinsForChange(n % largest, denoms[1:])
    localSolution = -1 if -1 == additionalNeeded else coinsAdded + additionalNeeded
    subSulution = minNumberOfCoinsForChange(n, denoms[1:])
    if localSolution > 0 and subSulution > 0:
        return min(localSolution, subSulution)
    else:
        return max(localSolution, subSulution)
