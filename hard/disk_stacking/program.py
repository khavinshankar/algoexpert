# time = O(n^2) and space = O(n)
def diskStacking(disks):
    disks.sort(key=lambda x: x[-1])
    
    heights = [disk[-1] for disk in disks]
    stacks = [None for disk in disks]
    max_height_i = 0 
    for i in range(1, len(disks)):
        curr_disk = disks[i]
        for j in range(i):
            prev_disk = disks[j]
            if (curr_disk[0] > prev_disk[0] and 
                curr_disk[1] > prev_disk[1] and 
                curr_disk[2] > prev_disk[2]):
                if heights[i] <= heights[j] + curr_disk[2]:
                    heights[i] = heights[j] + curr_disk[2]
                    stacks[i] = j
        if heights[i] >= heights[max_height_i]: max_height_i = i
    
    return getMaxStack(disks, stacks, max_height_i)

def getMaxStack(disks, stacks, i):
    max_stack = []
    while i is not None:
        max_stack.append(disks[i])
        i = stacks[i]
    
    return list(reversed(max_stack))