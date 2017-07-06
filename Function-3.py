import math
def roots(a,b,c):
    if((b*b-4*a*c)<0):
        print("The roots are non-real")
    else:
        x1=(-b+(b*b-4*a*c)**(0.5))/(2*a)
        x2=(-b-(b*b-4*a*c)**(0.5))/(2*a)
        print(x1)
        print(x2)
x=int(input())
y=int(input())
z=int(input())
roots(x,y,z)
