
#Stores a value for user name and password
user_name="BAHBARI"
password="GROCKAI"
#Initial number of trials which increases as the user inputs any wrong detail
trial=0
#looping the code while the number of trials is still less than 3
while trial<3:
    #The user enters his user name and password
    name=input("Enter user name: ").upper()
    password_1=input("Enter your password: ").upper()
    #when the user enters the correct user name and password, it pulls out of the while loop
    if name==user_name and password_1==password:
        print("✅Welcome, hope you're having a great day?")
        break
    #the rest of the conditional statement request for another input if any of the required details is wrong
    #It tells the user which of the dadtails are wrong.
    elif name==user_name and password_1!=password:
        print("❌ correct user name but incorrect password.")
    elif name!= user_name and password_1==password:
        print("❌ username is incorrect but password is correct.")
    else:
        print("❌ in correct user name and password.")
    #The trial variable increases when the user gets any detail wrong.
    trial+=1
#When the number of trials has reached 3, it blocks user access.
if trial==3:
    print("Sorry, you're out of trials.")