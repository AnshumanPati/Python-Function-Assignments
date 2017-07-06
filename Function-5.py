from random import randrange
def roll_dice(n,m):
    a=[]
    for i in range(m):
        a.append(randrange(1,n+1))
    print(a)
    return("That's all")
x=int(input())
y=int(input())
print(roll_dice(x,y))
if(x<4):
    print("Error!")
