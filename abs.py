from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        return 0
class rectange():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class square():
    def __init__(self,s):
        self.s=s
    def area(self):
        return self.s*self.s
rec=rectange(2,3)
square=square(2)
print(rec.area(),"and",square.area())