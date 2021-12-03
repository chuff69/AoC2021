
mask = [2048,1024,512,256,128,64,32,16,8,4,2,1]
bitcnt = {}
currentAddr = 0
binmask = ""
result = []
gamma = ""
epsilon = ""
count = 0
#Initialise bitcnt
for key in mask:
    val = 0
    bitcnt[key] = val

#Read file and count occurances of each bit
with open(r"C:\Users\Steven.Clough\OneDrive - Cinos Limited\Desktop\Advent of code\3\text.txt") as f:
    for line in f:
        currentStr = line.strip('\n')
        for key in mask:
            binmask = "{0:b}".format(key)                       #puts key into binary string
            currentAddr = (int(currentStr,2) & int(binmask,2))  #AND gate
            if currentAddr > 0:                                 #if AND bit set, increment bitcnt
                bitcnt[key] = bitcnt[key] + 1 


for val in bitcnt.values():
    if val >= 500:
        result.append(1)
    else:
        result.append(0)

for e in result:
    gamma = gamma + str(e)


gammaint = int(gamma, 2)                            #convert to int for XOR
inverse_s = gammaint ^ (2 ** (len(gamma) + 1) - 1)  # XOR
epsilon = bin(inverse_s)[3 : ]                  #convert back to binarystr
epsilonint = int(epsilon,2)

answer = gammaint * epsilonint
print(answer)
