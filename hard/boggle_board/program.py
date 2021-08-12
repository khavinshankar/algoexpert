# time = O(mn * 8^s + ws) and space = O(nm + ws) => m = len(col), n = len(row), w = len(words), s = max(len(word))
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    
    found = set()
    visited = [[False for char in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            search(i, j, board, trie.root, visited, found)
    return found

def search(i, j, board, trie_node, visited, found):
    if visited[i][j]: return
    
    char = board[i][j]
    if char not in trie_node: return

    visited[i][j] = True
    trie_node = trie_node[char]
    if "*" in trie_node: found.add(trie_node["*"])

    neighbors = getNeighbours(i, j, board)
    for x, y in neighbors: search(x, y, board, trie_node, visited, found)

    visited[i][j] = False

def getNeighbours(i, j, board):
    c = len(board)
    r = len(board[0])
    
    neighbors = []
    if i-1 >= 0: neighbors.append((i-1, j))
    if i+1 < c: neighbors.append((i+1, j))
    if j-1 >= 0: neighbors.append((i, j-1))
    if j+1 < r: neighbors.append((i, j+1))
    if i-1 >= 0 and j-1 >= 0: neighbors.append((i-1, j-1))
    if i-1 >= 0 and j+1 < r: neighbors.append((i-1, j+1))
    if i+1 < c and j-1 >= 0: neighbors.append((i+1, j-1))
    if i+1 < c and j+1 < r: neighbors.append((i+1, j+1))

    return neighbors

class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"
    
    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr: curr[char] = {}
            curr = curr[char]
        curr[self.end] = word

