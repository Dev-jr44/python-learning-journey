largest_number=float('-inf')
counter=0

while True:
    number=int(input("Enter number or type -1 to end the program: "))
    if number==-1:
        break
    counter +=1
    if number>largest_number:
        largest_number=number
if counter!=0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number")