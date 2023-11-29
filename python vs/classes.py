class employee:
    def __init__(self, name, contact, depa, salary):
        self._name = name
        self._contact = contact
        self._department = depa
        self._salary = salary
        
    def info(self):
        print(f"\nname = {self._name}")
        print(f"contact = {self._contact}")
        print(f"department = {self._department}")
        print(f"salary = {self._salary}")

class devloper(employee):
    def __init__(self, name, contact, type):
        employee.__init__(self, name, contact, salary = 80000, depa = "devlopers department")
        self._type = type
    def info(self):
        employee.info(self)
        print(f"devloper type = {self._type}\n")

e1 = employee("mohan", 1294852343, "debuggers department", 60000)
e1.info()
print()
d1 = devloper("sohan", 1576422323, "web devloper")
d1.info()