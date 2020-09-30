from collections import Counter
word = input("Enter a word")
dic={}
lk=[]
lv=[]
dic=Counter(word)
print(dic)
for i in dic.keys():
    lk.append(i)
for j in dic.values():
    lv.append(j)
for i in range(0,len(lv)):
    print(lk[i], " ", lv[i])
