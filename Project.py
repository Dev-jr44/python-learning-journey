even_number=0
odd_number=0

#input for first number
number=int(input("Enter an integer or type 0 to stop: "))

#when number isn't zero, we put this to abort the while loop else it will run forever
while number !=0:
    #if the number isn't divisible by 2, then it's odd
    if number%2==1:
        #update odd number
        odd_number +=1
    #else here meaning, if it is divisile by two then it's even
    else:
        #update even number
        even_number +=1
    #request for the second number, and run the while loop again as far as the "number" variable isn't zero 
    number=int(input("Enter an integer or type 0 to stop: "))
#when "0", has been inputed, it aborts the while loop and prints the answers
print("The number of even numbers are", even_number)
print("The number of odd numbers are", odd_number)

