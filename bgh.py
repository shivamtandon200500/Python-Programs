T = int(input())
class abc:
    def inp(n1):
        l=[]
        for i in range(0,n1):
            item=input()
            l.append(item)
        return l

    def check(lst):
        l = len(lst)
        i = 0
        while i < l - 1 and lst[i] >= lst[i + 1]:
            i += 1
        while i < l - 1 and lst[i] <= lst[i + 1]:
            i += 1
        return "Yes" if i == l - 1 else ("No")
l1=[]
for i in range(0,T):
    n = int(input())
    item2=abc.inp(n)
    l1.append(item2)
    print(l1)
    for j in range(0,len(l1)):
        x=abc.check(l1[j])
        print(x)