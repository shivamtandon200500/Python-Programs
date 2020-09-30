class abc:
    def __init__(self,name,salary,kam):
        self.name=name
        self.salary=salary
        self.kam=kam
    def __add__(self, other):
        return self.salary+other.salary
Shivam=abc("Shivam",2000,"pp")
Kopal=abc("Kopal",10000,"ww")
print(Shivam+Kopal)