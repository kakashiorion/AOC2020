import math

reachTime=1000390
x=-1
bus=[23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,503,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37]

eligibleBus=[]
order={}
remainders={}
index=0
for item in bus:
    if item!=x:
        eligibleBus.append(item)
        order[item]=index
        if index==0:
            remainders[item]=0
        elif item>index:
            remainders[item]=item-index
        elif item<index:
            remainders[item]=item-(index%item)
    index+=1

print('Eligible:', eligibleBus)

times={}
for i in eligibleBus:
    t=i-(reachTime%i)
    times[i]=t

smallest=1000
b=0
for j in times:
    if times[j]<smallest:
        b=j
        smallest=times[j]
print(b*smallest)
#part1:2298

print("Order:",order)
#s1:Find remainders (Bi)
print("Remainders",remainders)

#s2:Find semi-products(Ni)
product=1
for item in order:
    product*=item
print("Product(N):", product)
products={}
for item in order:
    products[item]=int(product/item)
print("Products:", products)

#s3:Find inverses (Xi)
inverses={}
for item in order:
    for i in range(1,item):
        if (products[item]*i) % item ==1:
            inverses[item]=i
            break
print("Inverses:", inverses)

#s4:Multiply Bi,Ni,Xi and add them to get X
multiplies={}
totalX=0
for item in order:
    f=products[item]*remainders[item]*inverses[item]
    multiplies[item]=f
    totalX+=f
print("Multiplies(B,N,X):", multiplies)
print("Total X:", totalX)

#s5:find X modulo product (N)
final=totalX%product
print("Final:", final)
#part2:783685719679632

