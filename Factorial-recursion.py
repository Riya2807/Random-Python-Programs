# Using Recursive Method
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
n=int(input("Enter a number:"))
print(factorial_recursive(n))