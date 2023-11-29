class org:
    def __init__(self, value):
        self.value = value
    
    def show(self):
        print(f"value is {self.value}")    
    
    @property #getter
    def ten_value(self):
        return 10 * self.value
    
    @ten_value.setter
    def ten_value(self, new):
        self.value = new

a = org(50)
# a.ten_value = 10
print(a.ten_value)
a.show()
