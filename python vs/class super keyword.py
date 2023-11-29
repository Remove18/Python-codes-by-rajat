class employee:
    def __init__(self, name, depart, sallery):
        self.name = name
        self.department = depart
        self.sallery = int(sallery)
    
    def show(self):
        print(f"{self.name} from {self.department} in {self.sallery}")
        
class head_emp(employee):
    def __init__(self, name, depart, sallery, post):
        super().__init__(name, depart, sallery)
        self.post = post
        
    def show(self):
        print(f"{self.post}")
        super().show()
        
a= head_emp("rajat", "devlopment department", 80000, "head devloper")
a.show()