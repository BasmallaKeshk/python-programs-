#B=[-10,8,-1,7,-14,-15,10]
'''
B=[10,8,-1,7,14,]

i=0
y=1
product=0
max_product=0
for i in range(0,len(B)):
    for y in range(i+1,len(B)):
        product=B[i]*B[y]
        if product > max_product:
            max_product=product
            y=y+1
    i=i+1
print(max_product)
'''
'''
#B=[9,6,2,10,5]
B=[-10,8,-1,7,14,-15,10]
i=0

max_element1=0
max_element2=0
min_element1=0
min_element2=0
max_product=0
for i in range(0,len(B)):
    max_element1=max(B)
    min_element1=min(B)
B.remove(max_element1)
B.remove(min_element1)
for i in range(0,len(B)):
    max_element2=max(B)
    min_element2=min(B)
if max_element1*max_element2 > min_element1*min_element2:
    max_product=max_element1*max_element2
else:
     max_product=min_element1*min_element2
print(max_product)
'''

B=[-10,8,-1,7,14,-15,10]
i=0

max_element1=0
max_element2=0
min_element1=0
min_element2=0
max_product=0

max_element1=max(B)
min_element1=min(B)
B.remove(max_element1)
B.remove(min_element1)

max_element2=max(B)
min_element2=min(B)
if max_element1*max_element2 > min_element1*min_element2:
    max_product=max_element1*max_element2
else:
     max_product=min_element1*min_element2
print(max_product)

