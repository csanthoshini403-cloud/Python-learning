# class animals:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name}is eating")
# class prey(animals):
#     def feel(self):
#         print(f"{self.name} is feeling")
# class predator(animals):
#     def hunt(self):
#         print(f"{self.name}is hunting")
# class rabbit(prey):
#     pass
# class hawk(predator):
#     pass
# class fish(prey,predator):
#     pass
# rabbit = rabbit("Peter")
# hawk = hawk("Mighty eagle")
# fish = fish("Google")        

# rabbit.feel()
# hawk.hunt()
# fish.feel()
# fish.hunt()
# rabbit.eat()

#encapsulation
# class Bank:
#     def __init__(self):
#         self.__balance = 0
#     def deposit(self,dep_account):
#         print(f"bal = (self.__balance + dep_amount)")
# account = Bank()

# account.deposit(100)        
 
 #static method
#  class Calculator:
#     def biggest(a,b):
#         if a>b:
#             return "a is greater"
#         else:
#             return "b is greater"
# print (Calculator.biggest(10,6))                

class student:
    count = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
    def get_info(self):
        print(f"{self.name} got a good {self.gpa} gpa")
    def got_count(cls):
        print(f"the number of students :{cls.count}")    
std1=student("Deva",8.98)
std1=student("Hari",7.7)
std1=student("Giri",9.01)
std1.get_info()
std1.got_count()
