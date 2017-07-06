import math
def gpa(cr,gr,no):
    s=0
    p=0
    for i in range(no):
        s=s+cr[i]
        p=p+(cr[i]*gr[i])
    print(p/s)
c=[]
g=[]
n=int(input())
for j in range(n):
    c.append(int(input()))
    g.append(int(input()))
gpa(c,g,n)

