s='942387615'
l=[9,4,2,3,8,7,6,1,5]
# l=list(s)
# l=[3,8,9,1,2,5,4,6,7]

currentIndex=0

def move(l,cIndex):
    removedList=[]
    value=l[cIndex]
    if cIndex>len(l)-2:
        removedList.append(l.pop(0))
    else:
        removedList.append(l.pop(cIndex+1))
    if cIndex>len(l)-2:
        removedList.append(l.pop(0))
    else:
        removedList.append(l.pop(cIndex+1))
    if cIndex>len(l)-2:
        removedList.append(l.pop(0))
    else:
        removedList.append(l.pop(cIndex+1))
    if cIndex>len(l)-1:
        destinationCup=l[len(l)-1] - 1
    else:
        destinationCup=l[cIndex] - 1
    if destinationCup==0:
            destinationCup=len(l)+3
    
    while(destinationCup in removedList):
        destinationCup-=1
        if destinationCup==0:
            destinationCup=len(l)+3

    dIndex=l.index(destinationCup)
    l.insert(dIndex+1,removedList[0])
    l.insert(dIndex+2,removedList[1])
    l.insert(dIndex+3,removedList[2])
    newIndex=l.index(value)
    if newIndex==len(l)-1:
        return (l,0)
    else:
        return (l,newIndex+1)

for i in range(100):
    result=move(l,currentIndex)
    l=result[0]
    currentIndex=result[1]
    # print(l)

print(l)
#part1 - 36542897

#Part 2
l=[9,4,2,3,8,7,6,1,5]

for i in range(10,1000001):
    l.insert(i-1,i)

# for j in range(1000):
#     result=move(l,currentIndex)
#     l=result[0]
#     currentIndex=result[1]
#     # print(l[:50])

# index1=l.index(1)
# v1=l[index1+1]
# v2=l[index1+2]
# p=v1*v2
# print(p)

class Node:
    def __init__(self,v):
        self.value=v
        self.next=None

class LinkedList():
    def __init__(self):
        self.start=None
        self.end=None
        self.value_to_node = {}

    def __getitem__(self, v):
        return self.value_to_node[v]

ll=LinkedList()

for i in range(1000000):
    n=Node(l[i])
    if (i==0):
        ll.start=n
        ll.end=n
    else:
        ll.end.next=n
        ll.end=n
        if (i==1000000):
            ll.end.next=ll.start
    ll.value_to_node[i]=n

def move2(lList):
    a=lList.start.next
    b=lList.start.next.next
    c=lList.start.next.next.next
    d=lList.start.value-1
    if d==0:
        d=1000000
    # print(a,b,c)
    while d in (a.value, b.value, c.value):
        d-=1
        if d==0:
            d=1000000
    curr=lList[d]
    lList.end=lList.start
    lList.start=lList.end.next.next.next.next
    c.next=curr.next
    curr.next=a

for j in range(10000001):
    move2(ll)
    # if (j>100000):
    #     print(len(ll.value_to_node))

p=ll[1].next.value*ll[1].next.next.value
print(p)
