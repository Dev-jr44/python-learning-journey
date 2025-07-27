# Number Guessing Game
# The user must guess a predefined number, receiving hints until they get it right or quit.

# The correct number to guess
correct_number = 123  

# Infinite loop until correct guess or exit
while True:
    try:
        # Prompt user for input and convert to integer
        user_input = int(input("Guess the correct number or enter 0 to exit: "))

        # Exit condition: user enters 0
        if user_input == 0:
            print("Game exited.")
            break  

        # Winning condition: correct guess
        elif user_input == correct_number:
            print("Correct ✅✅")
            break  

        # Hint system: feedback based on proximity to correct number
        elif user_input in range(1, 50):
            print("Too low, try again.")
        elif user_input in range(50, 80):
            print("Low, try again.")
        elif user_input in range(80, 100):
            print("Closer.")
        elif user_input in range(100, 123):
            print("Very close, try again.")
        elif user_input in range(124, 130):  
            print("Very close, try again.")
        elif user_input in range(130, 170):
            print("Too high, try again.")
        
        # Catch-all for invalid guesses (too low, too high, or non-relevant numbers)
        else:
            print("Way off! Try again.")

    # Handle non-integer input gracefully
    except ValueError:
        print("Enter an integer.")