master=[
'##.#...#',
'#..##...',
'....#..#',
'....####',
'#.#....#',
'###.#.#.',
'.#.#.#..',
'.#.....#']

#PART 1
#Initialize
active='#'
inactive='.'
spaceActivity={}
for x in range(-7,15):
    for y in range(-7,15):
        for z in range(-7,8):
            spaceActivity[(x,y,z)]=inactive

#Starting position
for y in range(len(master)):
    for x in range(len(master[y])):
        spaceActivity[(x,y,0)]=master[y][x]

def countNeighbors(x,y,z):
    global spaceActivity
    count=0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                if spaceActivity[(i,j,k)]==active and (i!=x or j!=y or k!=z):
                    count+=1
    return count

#simulate space 6 times
for s in range(1,7):
    temp=spaceActivity.copy()
    for x in range(0-s,8+s):
        for y in range(0-s,8+s):
            for z in range(0-s,1+s):
                c=countNeighbors(x,y,z)
                if spaceActivity[(x,y,z)]==active and (c<2 or c>3):
                    temp[(x,y,z)]=inactive
                elif spaceActivity[(x,y,z)]==inactive and (c==3):
                    temp[(x,y,z)]=active
    spaceActivity=temp

total=0
for x in range(-7,15):
    for y in range(-7,15):
        for z in range(-7,8):
            if spaceActivity[(x,y,z)]==active:
                total+=1

print(total)
#part1:315

#PART 2
#Initialize
active='#'
inactive='.'
hyperActivity={}
for x in range(-7,15):
    for y in range(-7,15):
        for z in range(-7,8):
            for w in range(-7,8):
                hyperActivity[(x,y,z,w)]=inactive

#Starting position
for y in range(len(master)):
    for x in range(len(master[y])):
        hyperActivity[(x,y,0,0)]=master[y][x]

def countHyperNeighbors(x,y,z,w):
    global hyperActivity
    count=0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                for l in range(w-1,w+2):
                    if hyperActivity[(i,j,k,l)]==active and (i!=x or j!=y or k!=z or l!=w):
                        count+=1
    return count

#simulate hypercube 6 times
for s in range(1,7):
    temp=hyperActivity.copy()
    for x in range(0-s,8+s):
        for y in range(0-s,8+s):
            for z in range(0-s,1+s):
                for w in range(0-s,1+s):
                    c=countHyperNeighbors(x,y,z,w)
                    if hyperActivity[(x,y,z,w)]==active and (c<2 or c>3):
                        temp[(x,y,z,w)]=inactive
                    elif hyperActivity[(x,y,z,w)]==inactive and (c==3):
                        temp[(x,y,z,w)]=active
    hyperActivity=temp

total=0
for x in range(-7,15):
    for y in range(-7,15):
        for z in range(-7,8):
            for w in range(-7,8):
                if hyperActivity[(x,y,z,w)]==active:
                    total+=1

print(total)
#part2:1520
