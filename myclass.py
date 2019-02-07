class Box:
    def __init__(self,a=200,b=100,h=300):
        self.a=a
        self.b=b
        self.h=h
        
    def volume(self):
            return self.a*self.b*self.h
box1=Box()
print(box1.a)
print(box1.b)
box1=Box(100,50,60)
print(box1.h)
print(box1.volume())

def get(self):
    return self.h
clr=Box()
print(clr.h)
