# Using Iterative Method
def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return(fac)
n=int(input("Enter a number:"))
print(factorial_iterative(n))