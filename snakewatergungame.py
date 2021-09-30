import random
n=0
u=0
comp=0
while n<10:
    cu= input("Enter:\n s for snake\n w for water \n g for gun\n Enter your choice:")
    lst= ["s","w","g"]
    cm= random.choice(lst)
    if cu=="s" and cm=="g":
        comp= comp+1
    elif cu=="s" and cm=="w":
        u= u+1
    elif cu=="s" and cm=="s":
        u= u+1
        comp= comp+1
    elif cu=="w" and cm=="s":
        comp= comp+1
    elif cu=="w" and cm=="w":
        u= u+1
        comp= comp+1
    elif cu=="w" and cm=="g":
        u= u+1
    elif cu=="g" and cm=="s":
        u= u+1
    elif cu=="g" and cm=="w":
        comp = comp+1   
    elif cu=="g" and cm=="g":
        u= u+1
        comp= comp+1
    n= n+1
if u>comp:
    print("The winner is---USER !!")
elif comp>u:
    print("The COMPUTER WINS ! Better luck next time <3")
elif u==comp:
    print("DRAW !!")
a="The scores are as follows:\n User={} \n Computer={}"
b=a.format(u,comp)
print(b)