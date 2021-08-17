# time = O(n + m) and space = O(m) => n = len(string) | m = len(substring) 
def knuthMorrisPrattAlgorithm(string, substring):
    pattern = getPattern(substring)
    return isAMatch(string, substring, pattern)

def isAMatch(string, substring, pattern):
    i = j = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            i += 1
            j += 1
            if j == len(substring): return True
        elif j > 0: j = pattern[j-1] + 1
        else: i += 1

    return False

def getPattern(string):
    pattern = [-1]
    
    i = 0; j = 1
    while j < len(string):
        if string[i] == string[j]:
            pattern.append(i)
            i += 1
        else:
            i = pattern[i-1] + 1
            if string[i] == string[j]:
                pattern.append(i)
                i += 1
            else:
                pattern.append(-1)
                i = 0
        j += 1
    
    return pattern