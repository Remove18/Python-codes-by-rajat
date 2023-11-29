class student:
    def __init__(self, name, c, g):
        self._name = name
        self._class = c
        self._gender = g
    
    def info(self):
        print(f"name is {self._name}")
        print(f"class is {self._class}")
        print(f"gender is {self._gender}")
    
    @staticmethod
    def add(a, b):
        return a + b
        
a = student("Rajat","BCA 2nd","Male")
a.info()
print(a.add(15,20))