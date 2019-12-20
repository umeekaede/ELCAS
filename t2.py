def solv_quadratic_equation(a, b, c):
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return [x_1, x_2]

v_prime=2.6e+8 # m/s
c=3.0e+8 # m/s

l=0.30 # m sin length
L=0.15 # m btw sts
t=0.5*10**(-9)  #s 30cm/1ns


a=4*((v_prime/c)**2-1)
b=4*(2*v_prime*t-l)
c=(4*(L*v_prime/c)**2)-4*(v_prime*t)**2-l**2+4*v_prime*t*l

ans=solv_quadratic_equation(a, b, c)

cl=input()  # criteria level
print("x1={0}, x2={1}".format(min(ans[0], ans[1]), max(ans[0], ans[1]) ))

if adc > cl: #adc is inputed by reading file
    print(min(ans[0], ans[1]))
else:
    print(max(ans[0], ans[1]))
