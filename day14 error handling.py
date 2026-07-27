#ASSIGNMENT DAY14
#PROBLEM-1
#DIVIDE TWO NUMBERS
try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    print("result:",a/b)
except ZeroDivisionError:
    print("cannot divide the numbers")
#PROBLEM-2
# INTEGER OUTPUT
try:
    age=int(input("enter the age:"))
    print("age=",age)
except ValueError:
    print("please enter the valid number")
#PROBLEM-3
# LIST INDEX
list=["egg","cup","bowl"]
try:
    index=int(input("enter the index"))
    print("list:",list[index])    
except IndexError:
    print("Invalid index")
#problem-4
# AGE VALIDATION
class InvalidAgeError(Exception):
    pass  
try:
    age=int(input("enter the age:"))
    if age<18:
        raise InvalidAgeError("age must be 18 or above")
    print("eligible")
except InvalidAgeError as e:
    print(e)
#PROBLEM-5
# PASSWORD LENGTH
class WeakPasswordError(Exception):
    pass
try:
    password=input("enter password:")
    if len(password) < 8:
        raise WeakPasswordError("password must be above 8 characters")
        print("strong Password")
except WeakPasswordError as m:
    print(m)

     


