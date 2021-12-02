f = open("text.txt", "r")
sonarList = []
increaseCount = -1
lastValue = 0
for line in f: sonarList.append(int(line))
for i in sonarList:
    if i > lastValue:
        increaseCount=increaseCount + 1
        lastValue = i
    else:
        lastValue = i
print(increaseCount)
