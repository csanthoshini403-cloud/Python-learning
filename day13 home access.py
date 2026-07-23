def rec(n):
    if n==0:
        return
    rec(n-1)
    print(n)
rec(5)  

square=lambda x:x*2
print(square(6))

def mul(n):
    return n*2
b=[1,2,3,4,5,6]
r=list(map(mul,b))
print(r)    

g=[1,2,3,4,5,6]
e_n=list(filter(lambda x:x%2==0,g))
print(e_n)

def odd(n):
    return n%2!=0
def square(n):
    return n*n
n=[1,2,3,4,56]
result=list(map(square,filter(odd,n)))
print(result)         