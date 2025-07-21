print("This program tests a hypothesis by a German mathematician named Lothar Collatz, which states:")
print("""
1.  Take any positive integer and call it c0;
2.  If it's even, set c0 to c0 ÷ 2;
3.  If it's odd, set c0 to 3 × c0 + 1;
4.  Repeat steps 2–3 until c0 becomes 1.
""")

# Prompt the user to enter a valid positive integer
while True:
    try:
        c0 = int(input("Enter any positive integer: "))
        if c0 > 0:
            break
        else:
            print("Number must be greater than 0. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Initialize the step counter
steps = 0

# Apply the Collatz operations until c0 becomes 1
while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        # If c0 is even, divide it by 2
        c0 //= 2
    else:
        # If c0 is odd, multiply by 3 and add 1
        c0 = 3 * c0 + 1
    steps += 1  # Increment the step count

# Print the final value and total steps taken
print("1")
print("Total steps:", steps)
