class student:
    def __init__(self, rollno, name, _class):
        self.roll_no= int(rollno)
        self.name= name
        self._class= _class
    
    def show(self):
        print(f"{self.roll_no}/ {self.name} from {self._class}")

class teacher(student):
    def __init__(self, number, name, _class):
        super().__init__(number, name, _class)  #key word

a = student(21, "rajat", "bca 2nd")
a.show()

# print(dir(student))  #method
# print(a.__dict__)  #method
# print(help(a))  #method

b = teacher(1, "golu","bca 2nd")
print(f"And {b.name} is the teacher of {b._class}")