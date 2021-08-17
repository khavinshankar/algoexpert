# time = O(c1 + c2) and space = O(c1 + c2)
def calendarMatching(calendar1, bound1, calendar2, bound2, duration):
    calendar1 = [["0:00", bound1[0]], *calendar1, [bound1[1], "23:59"]]
    calendar2 = [["0:00", bound2[0]], *calendar2, [bound2[1], "23:59"]]

    times1 = [[toMinutes(start), toMinutes(end)] for start, end in calendar1]
    times2 = [[toMinutes(start), toMinutes(end)] for start, end in calendar2]

    merged = merge(times1, times2)
    flattened = flatten(merged)

    availability = []
    for i in range(1, len(flattened)):
        start1, end1 = flattened[i-1]
        start2, end2 = flattened[i]

        if start2 - end1 >= duration:
            availability.append([end1, start2])
    
    return [[toTime(start), toTime(end)] for start, end in availability]

def flatten(merged):
    flattened = [merged[0]]
    for start, end in merged:
        if start <= flattened[-1][1]: flattened[-1][1] = max(flattened[-1][1], end)
        else:
            flattened.append([start, end])
    
    return flattened

def merge(times1, times2):
    merged = []

    i = j = 0
    while i < len(times1) and j < len(times2):
        if times1[i][0] < times2[j][0]:
            merged.append(times1[i])
            i += 1
        else:
            merged.append(times2[j])
            j += 1
    while i < len(times1):
        merged.append(times1[i])
        i += 1
    while j < len(times2):
        merged.append(times2[j])
        j += 1
    
    return merged

def toMinutes(time):
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)

def toTime(minutes):
    hours = str(minutes // 60)
    minutes = str(minutes % 60)
    return f"{hours}:{'0'+minutes if len(minutes) == 1 else minutes}"