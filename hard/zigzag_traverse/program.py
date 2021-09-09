# time = O(n) and space = O(n)
def zigzagTraverse(array):
    rows = len(array)
    cols = len(array[0])
    r = c = 0
    going_down = True
    answer = []
    while r >= 0 and c >= 0 and r < rows and c < cols:
        answer.append(array[r][c])
        if going_down:
            if c == 0 or r == rows - 1:
                going_down = False
                if r == rows - 1:
                    c += 1
                else:
                    r += 1
            else:
                r += 1
                c -= 1
        else:
            if r == 0 or c == cols - 1:
                going_down = True
                if c == cols - 1:
                    r += 1
                else:
                    c += 1
            else:
                r -= 1
                c += 1

    return answer