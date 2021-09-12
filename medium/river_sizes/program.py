# time = O(hw) and space = O(hw)
def riverSizes(matrix):
    h = len(matrix)
    w = len(matrix[0])
    visited = [[False for j in range(w)] for i in range(h)]
    river_sizes = []
    for i in range(h):
        for j in range(w):
            river_size = riverSize(i, j, matrix, visited)
            if river_size: river_sizes.append(river_size)
    
    return river_sizes

def riverSize(i, j, matrix, visited):
    if matrix[i][j] == 0 or visited[i][j]: return 0

    river_size = 0
    stack = [[i, j]]
    while len(stack):
        i, j = stack.pop()
        river_size += 1
        stack += getValidNeighbours(i, j, matrix, visited)

    return river_size

def getValidNeighbours(i, j, matrix, visited):
    neighbors = []
    visited[i][j] = True
    if i-1 >= 0 and not visited[i-1][j] and matrix[i-1][j]:
        neighbors.append([i-1, j])
        visited[i-1][j] = True
    if i+1 < len(visited) and not visited[i+1][j] and matrix[i+1][j]:
        neighbors.append([i+1, j])
        visited[i+1][j] = True
    if j-1 >= 0 and not visited[i][j-1] and matrix[i][j-1]:
        neighbors.append([i, j-1])
        visited[i][j-1] = True
    if j+1 < len(visited[0]) and not visited[i][j+1] and matrix[i][j+1]:
        neighbors.append([i, j+1])
        visited[i][j+1] = True
    
    return neighbors