a= [7, 6, 8, 4, 5]
b= [2, 9, 10, 6, 8]


iterator_i=0#index to be itereted on the first list
y_iterator=0#index to be itereted on the second list 
sum_a=sum(a)#sum of the list(a) to be compared with the sum of the list in each iteration and find the maximum sum at the specific number of swaps
sum_a2=0#the variable to compare any sum with it and take the the maximum sum
number_swaps=0# variable of number of number of swaps 
max1=0#to save in it the maximum element in the list
element=0# variable to save in the copy of element wihch have the maximum sum if it is swapped
pos=0# position of element which it is swaps get the highest maximum
for y_iterator in range(0,len(b)):#outer loop to iterate on the second list and compare each elemnt with the smallest element in the first list
    if b[y_iterator]>= max1 and number_swaps<=2:# to check if the elemnt in list b is bigger than the max1 variable to save it in the max variable
         max1=b[y_iterator]# if the condition be true the elemnt will be in max1
         for iterator_i in range(0,len(a)):#inner loop to iterate on each elemnt in list (a)
             # to make swaping between two elemnts and get the sum and compare it with max_sum
             max1=b[y_iterator]
             temp=a[iterator_i]
             a[iterator_i]=max1
             sum_a2=sum(a)#variable to save in it the sum of list(a)
             if sum_a2>=sum_a and number_swaps <=2:# check if the variable sum_2 is bigger than or equal to the sum of the list(a) and check that the number of swaps does not get 0
                 sum_a=sum_a2# if the condition gets true the sum of the list a will be in the maximum sum
                 element=a[iterator_i]#to save in it the elemnet which get the maximum sum
                 pos=iterator_i  # to save in it the position of the element
             a[iterator_i]=temp#put the element to be swapped in temp variable
         a[pos]=element# put the highst elemnt in the rigth place
         number_swaps=number_swaps+1#increase the number of swaps ntil being 3 
         iterator_i=iterator_i+1# incraesing the index to move to another element
         print(a)
y_iterator=y_iterator+1#increasing the index of second list to move to another element    
print(sum_a)#printing the maximum sum 
# brute -force algorithm for question2 
