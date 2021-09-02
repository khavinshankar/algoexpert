# time = O(n) and space = O(1)
def minNumberOfJumps(array):
    reach = 0
    steps = 1
    jumps = 0
    for i in range(len(array)):
        if i == len(array) - 1: return jumps

        reach = max(reach, i + array[i])
        steps -= 1

        if steps == 0:
            jumps += 1
            steps = reach - i