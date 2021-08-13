def multiStringSearch(string, words):
    trie = Trie()
    for word in words:
        trie.add(word)

    found = {}
    for i in range(len(string)):
        search(string, i, trie, found)
    
    return [word in found for word in words]

def search(string, start, trie, found):
    curr = trie.root
    for i in range(start, len(string)):
        if string[i] not in curr: break
        curr = curr[string[i]]

        if trie.end in curr: found[curr[trie.end]] = True

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