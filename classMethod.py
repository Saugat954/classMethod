
class Employee:
    company = "Apple"
    def __init__ (self,name):
        self.name = name
    def show(self):
        print(f"My name is {self.name} and I work in {self.company}")

    @classmethod 
    def changeCompany(cls,newCompany):
        cls.company = newCompany


E1  = Employee("Saugat")
E1.show()

Employee.changeCompany("Tesla")
E1.show()

E2 = Employee("Bijaya")
E2.show()