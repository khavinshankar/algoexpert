# time = O(n^2 + m) and space = O(n + m) => n = len(string) | m = len(pattern)
def patternMatcher(pattern, string):
    pattern, switched = makeConsistentPattern(pattern)
    firsty, nx, ny = analysePattern(pattern)
    
    if ny != 0:
        for xlen in range(1, len(string)):
            ylen = (len(string) - xlen * nx) / ny
            if ylen <= 0 or ylen % 1 != 0: continue
            ylen = int(ylen)

            iy = firsty * xlen
            x = string[0 : xlen]
            y = string[iy : iy + ylen]
            
            curr_string = ""
            for char in pattern:
                if char == "x": curr_string += x
                else: curr_string += y
            
            if curr_string == string:
                return [y, x] if switched else [x, y]
    else:
        xlen = len(string) / nx
        if xlen % 1 == 0:
            xlen = int(xlen)
            x = string[0 : xlen]
            curr_string = x * nx

            if curr_string == string:
                return ["", x] if switched else [x, ""]
    
    return []



def makeConsistentPattern(pattern):
    if pattern[0] == "x": return pattern, False
    
    new_pattern = "" 
    for char in pattern:
        if char == "x": new_pattern += "y"
        else: new_pattern += "x"
    return new_pattern, True

def analysePattern(pattern):
    nx = ny = 0
    firsty = None
    for i, char in enumerate(pattern):
        if char == "y" and firsty == None:
            firsty = i
        
        if char == "x": nx += 1
        else: ny += 1
    
    return firsty, nx, ny