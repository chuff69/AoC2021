x = 0 # forward / backward
y = 0 # depth
a = 0 # aim

key = 0
with open("text.txt") as f:
    for line in f:
        dir, val = line.split() 
        if dir == 'forward':
            x = x + int(val)
            y = y + (a * int(val))
        if dir == 'down':
            # y = y + int(val) # Spot my deliberate mistake
            a = a + int(val)
        if dir == 'up':
            # y = y - int(val) # Spot my deliberate mistake
            a = a - int(val)

print("Distance= ", x , "Depth= " , y )

answer = x * y 
print(answer)
