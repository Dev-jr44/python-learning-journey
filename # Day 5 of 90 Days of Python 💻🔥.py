# Day 5 of 90 Days of Python 💻🔥
# Program: Pyramid Height Calculator 🧱
# Description: This program calculates the maximum height of a flat pyramid-shaped wall 
# using a given number of blocks. Each lower layer contains one block more than the one above.

# Ask the user for the number of blocks
blocks = int(input("Enter your number of blocks: "))

# Set the initial height to 0
height = 0

# The number of blocks needed for the first layer
needed = 1

# While we have enough blocks to build the next layer
while blocks >= needed:
    # Subtract the used blocks from the total
    blocks -= needed
    # Increase the number of blocks needed for the next layer
    needed += 1
    # Increase the height of the pyramid
    height += 1

# Print the final height of the pyramid
print("The height that can be built is:", height)
