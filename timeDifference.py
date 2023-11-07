times = ["00:03", "23:59", "12:03"]

def timeToInt(time):
    hours = time[0:2]
    min = time[3:5]
    total = int(hours)*60 + int(min)
    return total

def timeDifference(times):
    seen = [False] * (24 * 60)
    for time in times:
        n = timeToInt(time)
        if seen[n]:
            return 0
        seen[n] = True
    prev = -1
    minDiff = (24 * 60) + 1
    first = -1
    for i in range(0, len(seen)):
        if seen[i] == True:
            if prev!=-1:
                minDiff = min(minDiff, i-prev)
            else:
                first = i
            prev = i
    minDiff = min(minDiff, first + 1440 - prev)
    return minDiff

print(timeDifference(times))
    