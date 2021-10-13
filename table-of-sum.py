'''
Taking two numbers as an input from the user and printing the table of the 
sum of those numbers upto 10 iterations.
'''
a,b= map(int,input().split())
num_sum=a+b
print(num_sum)
for i in range(1,11):
    ans=num_sum*i
    print(num_sum,'*',i,'=',ans, '\n')