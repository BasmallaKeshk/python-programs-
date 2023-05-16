
a=[4,5,3,4,3]
mini_element=len(a)#minimum element variable has length of list to be compared with each mini elemnet to get minimum element
for index_i in range (0,len(a)):#first loop to iterate on the list and get the minimum element
    if mini_element>a[index_i]:#check if each element to get the minimum elemnt
       mini_element=a[index_i]#put the minimum element at the variable 
first_area1=mini_element*len(a)#variable to save the first maximum area
b_appended_list=[]# empty list to put in it elemnts after subtracting minimum one
for j_index in range (0,len(a)):#for loop to iterate on the list to append each substracted element in b_appended_list
    element=a[j_index]-mini_element
    b_appended_list.append(element)
area_max=0#variable to save second maximum area
maxi_area_list=0# variable to compare each area with another one to get second maximum area 
c=[]# empty list to append in it all elemnts except 0 into separate lists
dlist=[]# empty list to append in it all elemnts except any 1 element
o_iterator=0# iterator to use in loop to accses the lists in the dlist
m_iterator=0# iterator to use in loop to accses each element in each list in the c list
from itertools import groupby# import of grouby to use lambada expression to separate elemnts without zeros
c=[list(v) for key1,v in groupby(b_appended_list,key=lambda x: x !=0) if key1!=0]
for m_iterator in range(0,len(c)):# loop to iterate on each list in the c list
    for o_iterator in range(0,len(c[m_iterator])):# loop to accses each elelment in each list in c list 
        dlist=[xl for xl in c[m_iterator] if xl!=1]# loop to deleting any 1 element 
        empty_list=[]#empty list if the dlist be empty exit the loop
        if  dlist != empty_list:#check if dlist not be an empty list
           dlist_len=len(dlist)#get length
           min1=min(dlist)#get minimum element in the list
           area_max=min1*dlist_len#multiply minimum element by lengthof the list
           if area_max>maxi_area_list:#check if each max is bigger than maxi_area
              maxi_area_list=area_max#put the area in maxi_area_list
        else:
            print("")#pinting nothing if dlist - empty list
print(first_area1+maxi_area_list)#printing the output maximum area

'''
mini_element=len(a)
for index_i in range (0,len(a)):
    if mini_element>a[index_i]:
       mini_element=a[index_i]
first_area=mini_element*len(a)
appended_list=[]
for j_index in range (0,len(a)):
    element=a[j_index]-mini_element
    appended_list.append(element)
area_max=0
m_iterator=0
max_area_list=0
c=[]
dlist=[]
from itertools import groupby
c=[list(v) for key1,v in groupby(appended_list,key=lambda x: x !=0) if key1!=0]
for m_iterator in range(0,len(c)):
    dlist=[x_index for x_index in c[m_iterator] if x_index!=1]
    empty_list=[]
    if  dlist != empty_list:
        dlist_length=len(dlist)
        min1=min(dlist)
        area_max=min1*dlist_length
        if area_max>max_area_list:
            max_area_list=area_max
    else:
        print("")      
print(first_area+area_max)
'''    
 #a=[4,5,3,4,3]
#a=[3,3,4,6,6,5,6]
#a=[8,4,9,5,7,2,1]
#a=[3,4,5,4,3,4,5]#basmalla
#a=[5,4,4,3,2,3,3]#rewan

'''
b_appended_list=[]
for j_index in range (0,len(a)):
    element=a[j_index]-mini_element
    b_appended_list.append(element)
area_max=0
maxi_area_list=0 
c=[]
dlist=[]
o_iterator=0
m_iterator=0
from itertools import groupby
c=[list(v) for key1,v in groupby(b_appended_list,key=lambda x: x !=0) if key1!=0]
for m_iterator in range(0,len(c)):
    for o_iterator in range(0,len(c[m_iterator])): 
        dlist=[xl for xl in c[m_iterator] if xl!=1]
        empty_list=[]
        if  dlist != empty_list:
           dlist_len=len(dlist)
           min1=min(dlist)
           area_max=min1*dlist_len
           if area_max>maxi_area_list:
              maxi_area_list=area_max
        else:
            print("")
print(first_area1+area_max)
'''
