# time = O(n(m^2) + nlogn) and space = O(nm) => n = len(strings) | m = max(len(string))
def longestStringChain(strings):
    strings.sort(key=len)
    
    record = {}
    last = ("", 0)
    for string in strings:
        record[string] = ("", 0)
        for i in range(len(string)):
            substring = string[0:i] + string[i+1:]
            if substring in record:
                if record[substring][1] >= record[string][1]:
                    record[string] = (substring, record[substring][1]+1)
                    if record[string][1] >= last[1]: last = (string, record[string][1]+1)
                        
    string_chain = []
    string = last[0]
    while string:
        string_chain.append(string)
        string = record[string][0]

    return string_chain