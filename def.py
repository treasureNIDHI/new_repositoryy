"creating function for some maths problems"
def sum_(x,y):
    #z=x+y
    return (x+y)
def diff(x,y):
    #z=abs(x-y)
    return (abs(x-y))
def sum_g(x,y):
    return (x*y)
def power(x,y):
    return (x**y)
def square(x):
    return (x**2)
enter=input("enter 'sum or diff or sum_g or power or square'")
n=int(input("enter a digit"))
m=int(input("enter another digit"))
if enter=='sum':
    print(sum_(n,m))
elif enter=="diff":
    print(diff(n,m))
elif enter=="sum_g":
    print(sum_g(n,m))
elif enter=="power":
    print(power(n,m))
elif enter=="square":
    a=int(input("enter the number"))
    print(square(a))
  
