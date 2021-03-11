adapters=['160',
'34',
'123',
'159',
'148',
'93',
'165',
'56',
'179',
'103',
'171',
'44',
'110',
'170',
'147',
'98',
'25',
'37',
'137',
'71',
'5',
'6',
'121',
'28',
'19',
'134',
'18',
'7',
'66',
'90',
'88',
'181',
'89',
'41',
'156',
'46',
'8',
'61',
'124',
'9',
'161',
'72',
'13',
'172',
'111',
'59',
'105',
'51',
'109',
'27',
'152',
'117',
'52',
'68',
'95',
'164',
'116',
'75',
'78',
'180',
'81',
'47',
'104',
'12',
'133',
'175',
'16',
'149',
'135',
'99',
'112',
'38',
'67',
'53',
'153',
'2',
'136',
'113',
'17',
'145',
'106',
'31',
'45',
'169',
'146',
'168',
'26',
'36',
'118',
'62',
'65',
'142',
'130',
'1',
'140',
'84',
'94',
'141',
'122',
'22',
'48',
'102',
'60',
'178',
'127',
'73',
'74',
'87',
'182',
'35']

q=[]
for x in adapters:
    q.append(int(x))
q.sort()
q.insert(0,0)
q.append(q[-1]+3)

print(q)

d={}
for j in range(len(q)-1):
    result=q[j+1]-q[j]
    if result in d:
        d[result]+=1
    else:
        d[result]=1

print(d[1]*d[3])
#part1:2738

# sample
# q=[0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
optional=[]
for i in range(1,len(q)):
    if q[i]-q[i-1]<3 and q[i+1]-q[i]<3:
        optional.append(q[i])
    
print('optionals:',optional)
print('total optionals',len(optional))
count=0
for k in range(1,len(optional)-1):
    if optional[k]-optional[k-1]==1 and optional[k+1]-optional[k]==1:
        count+=1
print('triplets:',count)

s=len(optional)-(count*3)
total=pow(2,s)*pow(7,count)
print('total:',total)
#part2:74049191673856
