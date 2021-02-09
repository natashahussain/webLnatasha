#Enter 2 lists of integers.Check
#(c) whether any value occur in both
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
  
lst1 = [1,3,5,2,6] 
lst2 = [9, 3,5,7] 
print("common elements of the lists are ",intersection(lst1, lst2)) 


  
 