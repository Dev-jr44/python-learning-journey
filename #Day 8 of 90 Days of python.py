#This is a program which requires a user input of numbers and stores it in a list
#When the user types 'done'
#It outputs the elements in the list, the total numbers entered,
#The sum and the average of the numbers.

#An empty list variable.
numbers=[]

#Keeps on looping till 'done' is typed.
while True:
    #Requests for a user input.
    user_input=input("Enter a number or type 'done' for exit: ")
    #Exits the loop if the user enters 'done'
    if user_input=='done':
        break
    #Checks if the user entered a valid number
    if user_input.isdigit():
        #Updates the list and changes the user input to an interger.
        numbers.append(int(user_input))
    else:
        print("Enter a valid number: ")
#Output.
print("You entered:",numbers)
print("Total numbers entered:",len(numbers))

print("The sum of the numbers is:",sum(numbers))
print("The average of the numbers are:",sum(numbers)/len(numbers))