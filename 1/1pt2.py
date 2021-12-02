sonarList = {}
key = 0
with open("text.txt") as f:
    for line in f:
        val = int(line.strip()) 
        sonarList[int(key)] = int(val)
        key = key + 1
d_length = (len(sonarList))
array_a = [1,2,3]
array_b = [2,3,4]
value_a = []
value_b = []
sum_a = 0
sum_b = 0
increase_count = -1
def get_values():
    for k in array_a:
        value_a.append(sonarList[k])
    for k in array_b:
        value_b.append(sonarList[k])

# Yes, this bit is broken - it doesn't compare the last set of values - I might fix this later.
count = 0
while count < d_length:
    count=count+1
    value_a = []
    value_b = []
    get_values()
    sum_a = sum(value_a)
    sum_b = sum(value_b)
    if sum_b > sum_a:
        increase_count=increase_count + 1
        array_a = [a + 1 for a in array_a]
        array_b = [b + 1 for b in array_b]
        print(array_a,array_b)
    else:
        array_a = [a + 1 for a in array_a]
        array_b = [b + 1 for b in array_b]
        print(array_a,array_b)

print(increase_count)
