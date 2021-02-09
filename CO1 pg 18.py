#Merge two dictionaries.

dict1 = {  'Anupama': 6, 'Sona': 12, 'John' : 10 }
dict2 = {'Aadithya': 8,'Sona': 20,}
dict3 = {**dict1 , **dict2}
print(dict3)