 #Enter 2 lists of integers.Check
#(b) whether list sums to same value
list1 = [2, 5, 4, 1, 6] 
list2 = [1, 6, 2, 3, 5]
print ("The first list is : "+ str(list1)) 
print ("The second list is : "+ str(list2))
total = sum(list1)
total2 = sum(list2)
print("Sum of all elements in given list 1: ", total)
print("Sum of all elements in given list 2: ", total2)
for i in range(0,len(list1) and len(list2)):
    if total==total2:
        print("Sum of values are same")
        break
    else:
        print("Sum of values are different")
        break
 





