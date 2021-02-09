#Sort dictionary in ascending and descending order.

y={'Natasha':21,'Dia':42,'Ammeera':14} 
                                       
lst=list(y.items()) 
print('original is :\n',lst)  

lst.sort()
print('Ascending order is :\n',lst)  

lst=list(y.items())
lst.sort(reverse=True)
print('Descending order is : \n',lst)

dict=dict(lst)
print("DICTIONARY :\n",dict) 