from functools import reduce
list1=[]
print("enter the no. those factorial is to be found")
n=int(input())
i=1
while(i<=n):
    list1.extend([i])
    i+=1
print(list1)
num=reduce(lambda x,y:x*y,list1)
print(num)