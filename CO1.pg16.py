#create a string separated with space and swap those at pos 1
w=input("Enter a string:")
s=w.split(" ")
for i in reversed(range(0,len(s))):
    print(s[i],end=" ")
