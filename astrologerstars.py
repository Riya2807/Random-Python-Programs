import struct
print struct.calcsize("P") * 8
n = int(input("Enter the desired number of rows:\n"))
b = int(input("Enter your choice: 0 or 1\n"))

if bool(b)== True:
    for i in range(1,n+1):
        print("*"*int(i))


elif bool(b)== False:
    for i in range(n,0,-1):
        print("*"*int(i))
    
    
