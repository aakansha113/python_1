list=[22,45,67,33,76]
print(type(list))       #type the  data structure of list   #list
print(list[1]) 

print(list[2:4])        #[67,33]

print(len(list))        #type the length of list (5) 

list.append(65)         #add elements at the end of the list   [22,45,67,33,76,65]
print(list)                                                  

list.sort()             #sort the list from ascending to descending order
print(list)

list.sort(reverse=True) # sort the list if the reverse is true the  output will be false  #False
print(list)

list.insert(3,50)       # insert the element at the given index here (index-3,element-50)  #[22,45,67,50,33,76]
print(list)
