from sympy import Symbol, solve
x=Symbol('x')
a=Symbol('a')
b=Symbol('b')
c=Symbol('c')
expr=a*x**2+b*x+c

ans=solve(expr,x, dict=True)
print(ans)
print(type(a))
