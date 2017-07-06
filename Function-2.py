import math
def yikes(x):
    e=2.71828
    return(x*(e**(-x))+(1-e**(-x))**(0.5))
a=int(input())
print(yikes(a))
