gnum=9
n=28
while(gnum>0):
    num= int(input("Guess the number:\n"))
    gnum=gnum-1
    print("Number of guesses left = ",gnum)
    if num>n:
        print("Enter a smaller number:\n")
        continue

    elif num==n:
        print("Congrats! You guessed the number correctly\n")
        print("You guessed the number correctly in",9-gnum,"guesses")
        break

    elif num<n:
        print("Enter a larger number:\n")
        continue
        
print("Game Over!!!!!")
