"creating function for some maths problems"
def sum_(x,y):
    z=x+y
    return z
def diff(x,y):
    z=abs(x-y)
    return z
def sum_g(x,y):
    return (x*y)
enter=input("enter 'sum or diff or sum_g'")
n=int(input("enter a digit"))
m=int(input("enter another digit"))
if enter=='sum':
    print(sum_(n,m))
elif enter=="diff":
    print(diff(n,m))
elif enter=="sum_g":
    print(sum_g(n,m))

  