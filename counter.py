str=input("Enter word")
c=0
n=input("enter letter to be count")
for item in str:
    if item!=n:
        continue
    else:
        c=c+1
print(c)