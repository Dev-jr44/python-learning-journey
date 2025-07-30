# Beatles Band Member Tracker
# This script builds a list of The Beatles' final band members through user input and list operations.

# Step 1: Create an empty list named 'beatles'
beatles = []

# Step 2: Add the first three permanent members to the list
members = ["John Lennon", "Paul McCartney", "George Harrison"]
for member in members:
    beatles.append(member)  # Add each member using append()

# Step 3: Ask the user to add two temporary members
for i in range(2):
    new_member = input("Enter the name of a temporary band member: ")
    beatles.append(new_member)  # Add the entered member to the list

# Step 4: Remove the last two members (temporary ones)
del beatles[-1]
del beatles[-1]

# Step 5: Insert Ringo Starr at the beginning of the list
beatles.insert(0, "Ringo Starr")

# Final Output
print("\nFinal list of band members:")
print(beatles)
