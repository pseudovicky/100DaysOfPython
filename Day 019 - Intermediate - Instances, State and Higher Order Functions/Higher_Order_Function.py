def addition(n1,n2):
    return n1+n2
def subtract(n1,n2):
     return n1-n2
def multiply(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1-n2

def calculator(n1, n2, func):
    return func(n1 , n2)

result = calculator(10,20,addition)
print(result)
