# time = O(n^2) and space = O(n)
def rectangleMania(coords):
    record = {}
    for x, y in coords:
        record[(x, y)] = True
        
    rectangles = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if x2 > x1 and y2 > y1:
                if (x1, y2) in record and (x2, y1) in record: rectangles += 1
    
    return rectangles