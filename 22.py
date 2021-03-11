deck=['Player 1:',
'6',
'25',
'8',
'24',
'30',
'46',
'42',
'32',
'27',
'48',
'5',
'2',
'14',
'28',
'37',
'17',
'9',
'22',
'40',
'33',
'3',
'50',
'47',
'19',
'41',
'',
'Player 2:',
'1',
'18',
'31',
'39',
'16',
'10',
'35',
'29',
'26',
'44',
'21',
'7',
'45',
'4',
'20',
'38',
'15',
'11',
'34',
'36',
'49',
'13',
'23',
'43',
'12']

p1Deck=[]
p2Deck=[]
for x in range(1,26):
    p1Deck.append(int(deck[x]))
for x in range(28,53):
    p2Deck.append(int(deck[x]))

def moveCombat(d1,d2):
    c1=d1.pop(0)
    c2=d2.pop(0)
    if c1<c2:
        d2.append(c2)
        d2.append(c1)
    if c1>c2:
        d1.append(c1)
        d1.append(c2)

def calcScore(d):
    result=0
    e=d.copy()
    i=1
    while(len(e)!=0):
        c=e.pop()
        result+=i*c
        i+=1
    return result

while (len(p1Deck)!=0 and len(p2Deck)!=0):
    moveCombat(p1Deck,p2Deck)

if len(p1Deck)==0:
    print('2',calcScore(p2Deck))
else:
    print('1', calcScore(p1Deck))
#part1:33559

#PART 2
p1Deck=[]
p2Deck=[]
for x in range(1,26):
    p1Deck.append(int(deck[x]))
for x in range(28,53):
    p2Deck.append(int(deck[x]))

r={}
def recursiveCombat(d1,d2,game):
    global r
    while (len(d1)!=0 and len(d2)!=0):
        if game in r and [d1,d2] in r[game]:
            # print('Player 1 wins game '+str(game))
            return 1
        else:
            x=[d1.copy(),d2.copy()]
            if game in r:
                r[game].append(x)
            else:
                r[game]=[x]
            c1=d1.pop(0)
            c2=d2.pop(0)
            if len(d1)>=c1 and len(d2)>=c2:
                game+=1
                if game in r:
                    game=len(r)+1
                roundWinner=recursiveCombat(d1[:c1].copy(),d2[:c2].copy(),game)
            else:
                if c1<c2:
                    roundWinner=2
                else:
                    roundWinner=1
            
            if roundWinner==1:
                # print('Player 1 wins round')
                d1.append(c1)
                d1.append(c2)
            else:
                d2.append(c2)
                d2.append(c1)

    if len(d1)==0:
        # print('Player 2 wins game '+str(game) +' with length '+str(len(d2)))
        return 2
    else:
        # print('Player 1 wins game '+str(game) +' with length '+str(len(d1)))
        return 1

finalWinner=recursiveCombat(p1Deck,p2Deck,1)
if finalWinner==1:
    print(calcScore(p1Deck))
elif finalWinner==2:
    print(calcScore(p2Deck))