class x:
    n = 10

    def use(l):
        for i in range(0, 10):
            l.append(i)
la=[]
x.use(la)
print(la)