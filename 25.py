cardPublic=9033205
doorPublic=9281649

subjectNumber=7
constNumber=20201227

loopSize=1
value=1
while (value!=cardPublic):
    value=value*subjectNumber
    value=value%constNumber
    loopSize+=1
cardLoopsize= loopSize-1
print('card',cardLoopsize)

loopSize=1
value=1
while (value!=doorPublic):
    value=value*subjectNumber
    value=value%constNumber
    loopSize+=1
doorLoopsize= loopSize-1
print('door', loopSize)

# cardLoopsize= 13467729
# doorLoopsize= 3020524

value=1
for i in range(doorLoopsize):
    value=value*cardPublic
    value=value%constNumber

print(value)

value=1
for i in range(cardLoopsize):
    value=value*doorPublic
    value=value%constNumber

print(value)
#part1:9714832