# time = O(n) and space = O(n)
def waterArea(walls):
    n = len(walls)
    left_max = [0]
    for i in range(n-1):
        if walls[i] > left_max[-1]: left_max.append(walls[i])
        else: left_max.append(left_max[-1])
    
    area = 0
    right_max = 0
    for i in range(n-1, 0, -1):
        storage = min(left_max[i], right_max)
        area += 0 if walls[i] >= storage else storage - walls[i] 
        right_max = max(right_max, walls[i])

    return area
