# time = O(w*nlogn) and space = O(wn) => w = len(words) | n = max(len(word))
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams: 
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
        
    return list(anagrams.values())