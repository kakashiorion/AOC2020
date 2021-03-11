originalNumbers=[1,2,16,19,18,0]

startingNumbers=originalNumbers.copy()

for x in range(2020):
    length=len(startingNumbers)
    lastSpoken=startingNumbers[length-1]
    if lastSpoken not in startingNumbers[:length-1]:
        startingNumbers.append(0)
    else:
        startingNumbers.reverse()
        age=startingNumbers[1:].index(lastSpoken)+1
        startingNumbers.reverse()
        startingNumbers.append(age)

print(startingNumbers[2019])
#part1:536

startingNumbers=originalNumbers.copy()
d={}
index=0
for i in startingNumbers:
    d[i]=index
    index+=1
print(d)
e={}
for x in range(30000000):
    length=len(startingNumbers)
    lastSpoken=startingNumbers[length-1]
    if lastSpoken not in e:
        startingNumbers.append(0)
        e[0]=d[0]
        d[0]=length
    else:
        age=d[lastSpoken]-e[lastSpoken]
        startingNumbers.append(age)
        e[lastSpoken]=d[lastSpoken]
        if age in d:
            e[age]=d[age]
        d[age]=length

print(startingNumbers[29999999])
#part2:24065124
