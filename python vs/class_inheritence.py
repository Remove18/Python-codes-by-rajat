class student:
    def __init__(self, rn, n, c, add):
        self._roll_num = rn
        self._name = n
        self._class = c
        self._address = add
        
class students(student):
    def info(self):
        print(f"student no. {self._roll_num} name {self._name} in {self._class}year from {self._address}")

# a1 = student(21,"rajat","bca 2nd","dmt")
# a1.info()
a2 = students(21,"rajat","bca 2nd","dmt")
a2.info()