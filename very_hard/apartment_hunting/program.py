import math

# time = O(br) and space = O(br)
def apartmentHunting(blocks, reqs):
    records = [{req: -1 for req in reqs} for block in blocks]

    for req in reqs: records[0][req] = 0 if blocks[0][req] else math.inf
    for i in range(1, len(blocks)):
        for req in reqs:
            if blocks[i][req]:
                records[i][req] = 0
            else:
                records[i][req] = records[i-1][req] + 1
    
    for i in range(len(blocks)-2, -1, -1):
        for req in reqs:
            if blocks[i][req]:
                records[i][req] = 0
            else:
                records[i][req] = min(records[i][req], records[i+1][req] + 1)
    
    min_distance = math.inf
    apartment_index = -1
    for i, record in enumerate(records):
        max_req = -1
        for req in reqs:
            max_req = max(max_req, record[req])
        
        if min_distance > max_req:
            min_distance = max_req
            apartment_index = i

    return apartment_index