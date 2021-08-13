# time = O(n(n+m)) and space = O(n) => n = len(string) | m = len(key)
def underscorifySubstring(string, key):
    locations = collapseLocations(getLocations(string, key))
    return underscorify(string, locations)
    
def getLocations(string, key):
    locations = []
    i = 0
    while i < len(string):
        location = string.find(key, i)
        if location == -1: break
        locations.append([location, location + len(key)])
        i = location + 1
    
    return locations
        
def collapseLocations(locations):
    if not len(locations): return []
    collapsed = [*locations[0]]
    for i in range(1, len(locations)):
        if locations[i][0] <= collapsed[-1]: collapsed[-1] = locations[i][1]
        else: collapsed.extend(locations[i])
    
    return collapsed

def underscorify(string, locations):
    underscorified = ""
    loc = 0
    for i in range(len(string)):
        if loc < len(locations) and i == locations[loc]:
            loc += 1
            underscorified += "_"
        underscorified += string[i]
    if loc < len(locations) and i+1 == locations[loc]: underscorified += "_"

    return underscorified