#magic methods

class employee:
    def __init__(self, name, sallary):
        self.name = name
        self.sallary = int(sallary)
        
    def show(self):
        print(f"{self.name}`s sallary is {self.sallary}")
    
    def __len__(self): #returns only inteser value #only returns not prints
        return len(self.name)
    
    def __call__(self):
        return "__call__ method activated" #only returns not prints
    
    def __str__(self):
        return "in __str__ method"
    
    def __repr__(self):
        return "in __repr__ method"
    
a = employee("rajat", 80000)
a.show()
print(len(a))
a()
print(a)
print(str(a))
print(repr(a))