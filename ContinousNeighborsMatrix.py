# You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s.
# Each 0 represents land, and each 1 represents part of a river. A river consists of any
# number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent).
# The number of adjacent 1s forming a river determine its size.
# Write a function that returns an array of the sizes of all rivers represented in the input matrix.
# Note that these sizes do not need to be in any particular order.

def continousNeighborSizes(matrix):
    sizes = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 1:
                size = 1
                matrix[x][y] = 0
                neighbors = getNeighbors(x, y, matrix)
                while len(neighbors) > 0:
                    coord = neighbors.pop()
                    size += 1
                    matrix[coord[0]][coord[1]] = 0
                    neighbors = neighbors + getNeighbors(coord[0], coord[1], matrix)
                sizes.append(size)
    return sizes


def getNeighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[x - 1][y] == 1:
        neighbors.append((x - 1, y))
        matrix[x - 1][y] = 0
    if y > 0 and matrix[x][y - 1] == 1:
        neighbors.append((x, y - 1))
        matrix[x][y - 1] = 0
    if x < len(matrix) - 1 and matrix[x + 1][y]:
        neighbors.append((x + 1, y))
        matrix[x + 1][y] = 0
    if y < len(matrix[x]) - 1 and matrix[x][y + 1]:
        neighbors.append((x, y + 1))
        matrix[x][y + 1] = 0
    return neighbors
