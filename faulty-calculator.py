'''
Solves all the problems except:
45*3=555
56+9=77
56/6=4

Takes two numbers and an operator as an input from the user and then returns the result
'''
a=int(input())
b=int(input())
o=input()
if a==45 and b==3 and o=='*':
    print('555')
elif a==56 and b==9 and o=='+':
    print('77')
elif a==56 and b==6 and o=='/':
    print('4')
else:
    if o=='+':
        print(a+b)
    elif o=='-':
        print(a-b)
    elif o=='/':
        print(a/b)
    elif o=='*':
        print(a*b)