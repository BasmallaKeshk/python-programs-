a=[7,6,8,4,5] 
b=[2,9,10,6,8] 
a.sort()#function sort to sort the list(a) as the smallest elements at the first of the array 
b.sort()# function sort is to sort list(b)as highest elemnts will be at the last of array
length=len(b)#variable to save the length of the second list
comparable=0#variable will be compared with number of swaps and will be incresed until the number of swaps
swaper=3# number of swaps
index_i=0 # index of each element in first list which will have smallest element 
index_y=length-1 # index of each element in the second list which will have highest element 
while comparable<swaper:#while loop will iterate util the number of swaps 
    if b[index_y]>a[index_i]:# check if the highest element in second list bigger then the first element in the first list
        #swaps between smallest element and higest element
        temp=a[index_i]#put smallest element in variable temp
        a[index_i]=b[index_y]#put the highest element in the place of smallest element
        b[index_y]=temp#put the element in temp in the place of higest element
    index_i=index_i+1#increasing the index of first list by 1
    index_y=index_y-1#decresing the index of second list by 1
    comparable=comparable+1# increasing the n variable until reaching to number of swaps
sum_first_list=sum(a)#variable to save in it the sum of the list
print("output : " ,sum_first_list )#displaying the sum of the list 

#effecincy of second question
