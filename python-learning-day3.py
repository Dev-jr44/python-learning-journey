#This program removes vowels "A,E,I,O,U" from a word entered by a user
#It uses conditional statements & continue

#Requests for an input from the user and convert it to uppercase
user_word=input("Enter a word: ").upper()
word_without_vowels=""
#processes each character in the user input
for letter in user_word:
    #skips current iteration if any letter is a vowel
    #using string membership test
    if letter in "AEIOU":
        continue #bypass vowel characters
    word_without_vowels+=letter
print(word_without_vowels)
    
