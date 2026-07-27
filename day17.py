class animals:
    def __init__(self,name,is_alive):
        self.name=name
        self.is_alive=is_alive
    def eat(self):
        print(f"{self.name} is eating")
class dog(animals):            
    pass
class cat(animals):
    pass
dog= dog("scooby","true")
cat=cat("dodo","true")
dog.eat()
cat.eat()
print(dog.name)
print(cat.name)
