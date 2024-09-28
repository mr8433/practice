class Person:
    name="Harry"
    occupation="Software Developer"
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
obj1=Person()
# obj1.name="Mayank"
# obj1.occupation="Accountant"

obj1.info()
